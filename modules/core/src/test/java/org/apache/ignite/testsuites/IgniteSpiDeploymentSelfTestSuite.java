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

package org.apache.ignite.testsuites;

import org.apache.ignite.spi.deployment.local.GridLocalDeploymentSpiSelfTest;
import org.apache.ignite.spi.deployment.local.GridLocalDeploymentSpiStartStopSelfTest;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

/**
 * Test suit for deployment SPIs.
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({
    GridLocalDeploymentSpiSelfTest.class,
    GridLocalDeploymentSpiStartStopSelfTest.class
})
public class IgniteSpiDeploymentSelfTestSuite {
}
