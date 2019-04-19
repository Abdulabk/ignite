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

package org.apache.ignite.internal.processors.metastorage.persistence;

import java.io.Serializable;

/**
 * Distributed metastorage data that joining node sends to cluster.
 */
@SuppressWarnings("PublicField")
class DistributedMetaStorageJoiningNodeData implements Serializable {
    /** */
    private static final long serialVersionUID = 0L;

    /**
     * Baseline topology id of node, {@code -1} if baseline topology is null.
     */
    public final int bltId;

    /**
     * Distributed metastorage version of joining node.
     */
    public final DistributedMetaStorageVersion ver;

    /**
     * Available history of joining node.
     */
    public final DistributedMetaStorageHistoryItem[] hist;

    /** */
    public DistributedMetaStorageJoiningNodeData(
        int bltId,
        DistributedMetaStorageVersion ver,
        DistributedMetaStorageHistoryItem[] hist
    ) {
        this.bltId = bltId;
        this.ver = ver;
        this.hist = hist;
    }
}
