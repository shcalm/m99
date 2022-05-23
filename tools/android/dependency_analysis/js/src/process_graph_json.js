// Copyright 2020 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import {GraphNode, PackageNode, ClassNode, GraphModel} from './graph_model.js';
import {shortenPackageName, shortenClassName} from './chrome_hooks.js';

/**
 * A graph read from JSON.
 * @typedef {Object} JsonGraph
 * @property {Array<Object>} nodes
 * @property {Array<Object>} edges
 */

/**
 * A function that creates a GraphNode object from node JSON data.
 * @callback MakeNodeFunction
 * @param {Object} node The node JSON data.
 * @return {!GraphNode} The constructed GraphNode.
 */

/**
 * Transforms a graph JSON generated by Python scripts
 * (generate_json_dependency_graph.py) into a working format for d3.
 * @param {!JsonGraph} jsonGraph The JSON graph to parse.
 * @param {!MakeNodeFunction} makeNode The function to create a node from JSON
 *     node data.
 * @return {!GraphModel} The parsed out GraphModel object.
 */
function parseGraphModelFromJson(jsonGraph, makeNode) {
  const graph = new GraphModel();
  for (const nodeData of jsonGraph.nodes) {
    graph.addNodeIfNew(makeNode(nodeData));
  }
  for (const edgeData of jsonGraph.edges) {
    // Assuming correctness of the JSON, we can assert non-null GraphNodes here.
    const /** !GraphNode */ beginNode = graph.getNodeById(edgeData.begin);
    const /** !GraphNode */ endNode = graph.getNodeById(edgeData.end);
    graph.addEdgeIfNew(beginNode, endNode);
  }
  return graph;
}


/**
 * Parses a package JSON graph generated by Python scripts.
 * @param {!JsonGraph} jsonGraph The JSON package graph to parse.
 * @return {!GraphModel} The parsed out GraphModel object.
 */
function parsePackageGraphModelFromJson(jsonGraph) {
  const makePackageNode = nodeData => new PackageNode(
      nodeData.name, shortenPackageName(nodeData.name), nodeData.meta.classes);
  return parseGraphModelFromJson(jsonGraph, makePackageNode);
}

/**
 * Parses a class JSON graph generated by Python scripts.
 * @param {!JsonGraph} jsonGraph The JSON class graph to parse.
 * @return {!GraphModel} The parsed out GraphModel object.
 */
function parseClassGraphModelFromJson(jsonGraph) {
  const makeClassNode = nodeData => new ClassNode(
      nodeData.name, shortenClassName(nodeData.name), nodeData.meta.package,
      nodeData.meta.build_targets);
  return parseGraphModelFromJson(jsonGraph, makeClassNode);
}

export {
  parsePackageGraphModelFromJson,
  parseClassGraphModelFromJson,
};
