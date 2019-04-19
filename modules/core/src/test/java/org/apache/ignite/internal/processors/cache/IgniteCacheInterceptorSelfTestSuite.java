/*
 * Copyright 2019 GridGain Systems, Inc. and Contributors.
 * 
 * Licensed under the GridGain Community Edition License (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     https://www.gridgain.com/products/software/community-edition/gridgain-community-edition-license
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.ignite.internal.processors.cache;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import org.apache.ignite.testframework.GridTestUtils;
import org.apache.ignite.testframework.junits.DynamicSuite;
import org.junit.runner.RunWith;

/**
 * Cache interceptor suite.
 */
@RunWith(DynamicSuite.class)
public class IgniteCacheInterceptorSelfTestSuite {
    /**
     * @return Cache API test suite.
     */
    public static List<Class<?>> suite() {
        return suite(null);
    }

    /**
     * @param ignoredTests Tests to ignore.
     * @return Test suite.
     */
    public static List<Class<?>> suite(Collection<Class> ignoredTests) {
        List<Class<?>> suite = new ArrayList<>();

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorLocalSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorLocalWithStoreSelfTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorLocalAtomicSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorLocalAtomicWithStoreSelfTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicNearEnabledSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicWithStoreSelfTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicReplicatedSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicWithStoreReplicatedSelfTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorNearEnabledSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorWithStoreSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorReplicatedSelfTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorReplicatedWithStoreSelfTest.class, ignoredTests);

// TODO GG-11141.
//        GridTestUtils.addTestIfNeeded(suite, GridCacheOnCopyFlagTxPartitionedSelfTest.class, ignoredTests);
//        GridTestUtils.addTestIfNeeded(suite, GridCacheOnCopyFlagReplicatedSelfTest.class, ignoredTests);
//        GridTestUtils.addTestIfNeeded(suite, GridCacheOnCopyFlagLocalSelfTest.class, ignoredTests);
//        GridTestUtils.addTestIfNeeded(suite, GridCacheOnCopyFlagAtomicSelfTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, CacheInterceptorPartitionCounterRandomOperationsTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, CacheInterceptorPartitionCounterLocalSanityTest.class, ignoredTests);

        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorAtomicRebalanceTest.class, ignoredTests);
        GridTestUtils.addTestIfNeeded(suite, GridCacheInterceptorTransactionalRebalanceTest.class, ignoredTests);

        return suite;
    }
}
