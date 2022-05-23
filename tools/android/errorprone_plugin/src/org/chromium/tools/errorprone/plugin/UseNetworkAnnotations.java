// Copyright 2021 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package org.chromium.tools.errorprone.plugin;

import static com.google.errorprone.matchers.Matchers.anyOf;
import static com.google.errorprone.matchers.Matchers.instanceMethod;

import com.google.auto.service.AutoService;
import com.google.errorprone.BugPattern;
import com.google.errorprone.VisitorState;
import com.google.errorprone.bugpatterns.BugChecker;
import com.google.errorprone.matchers.Description;
import com.google.errorprone.matchers.Matcher;
import com.google.errorprone.util.ASTHelpers;
import com.sun.source.tree.ExpressionTree;
import com.sun.source.tree.MethodInvocationTree;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * Checks for direct calls to blocklisted methods to make network requests. Chromium code should
 * use ChromiumNetworkAdapter instead, with a NetworkTrafficAnnotationTag documenting the
 * network request for static analysis.
 *
 * Currently, only URL#openConnection() is blocklisted by this BugChecker.
 */
@AutoService(BugChecker.class)
@BugPattern(name = "UseNetworkAnnotations",
        summary = "Use wrapper network APIs with NetworkTrafficAnnotationTag",
        severity = BugPattern.SeverityLevel.ERROR, linkType = BugPattern.LinkType.CUSTOM,
        link = "https://bugs.chromium.org/p/chromium/issues/detail?id=1231780")
public class UseNetworkAnnotations
        extends BugChecker implements BugChecker.MethodInvocationTreeMatcher {
    private static final String URL_CLASS_NAME = "java.net.URL";
    private static final String OPEN_CONNECTION_METHOD_NAME = "openConnection";

    private static final Matcher<ExpressionTree> METHOD_MATCHER =
            anyOf(instanceMethod()
                            .onDescendantOf(URL_CLASS_NAME)
                            .namedAnyOf(OPEN_CONNECTION_METHOD_NAME));

    /**
     * Allow-listed prefixes, starting relative to the src/ dir. It is OK to call
     * URL#openConnection() from Java code inside these directories, either because they're not
     * part of clank, or because they're //net implementation details.
     */
    private static final ArrayList<String> ALLOWLISTED_FILES = new ArrayList<>(
            List.of("net/android/java/src/org/chromium/net/ChromiumNetworkAdapter.java",
                    "android_webview/nonembedded/java/src/org/chromium/android_webview/nonembedded/"
                            + "NetworkFetcherTask.java",
                    "components/cronet/", "chromecast/", "clank/test/"));

    @Override
    public Description matchMethodInvocation(MethodInvocationTree tree, VisitorState state) {
        if (!METHOD_MATCHER.matches(tree, state)) {
            return Description.NO_MATCH;
        }

        // Find the src/ dir. This assumes the build path is inside the src/ directory, and that
        // the root is actually called "src".
        Path buildPath = Paths.get("").toAbsolutePath();
        Path srcDir = buildPath;
        while (srcDir != null && !srcDir.endsWith("src")) {
            srcDir = srcDir.getParent();
        }
        if (srcDir == null) {
            return buildDescription(tree)
                    .setMessage(
                            "Could not find the src/ directory for the UseNetworkAnnotations check."
                            + " Make sure your build path is inside src/.")
                    .build();
        }

        // Check whether the file is allowlisted.
        Path javaFile = Paths.get(ASTHelpers.getFileName(state.getPath().getCompilationUnit()));
        for (String allowed : ALLOWLISTED_FILES) {
            if (javaFile.startsWith(srcDir.resolve(allowed))) {
                return Description.NO_MATCH;
            }
        }

        return buildDescription(tree)
                .setMessage("Direct use of URL#openConnection() is forbidden in Chromium. Use "
                        + "ChromiumNetworkAdapter#openConnection() instead.")
                .build();
    }
}
