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

package org.apache.ignite.internal.util.lang.gridfunc;

import java.util.UUID;
import org.apache.ignite.cluster.ClusterNode;
import org.apache.ignite.internal.util.typedef.internal.S;
import org.apache.ignite.lang.IgnitePredicate;

/**
 * Creates grid node predicate evaluating on the given node ID.
 */
public class EqualsClusterNodeIdPredicate<T extends ClusterNode> implements IgnitePredicate<T> {
    /** */
    private static final long serialVersionUID = -7082730222779476623L;

    /** */
    private final UUID nodeId;

    /**
     * @param nodeId (Collection)
     */
    public EqualsClusterNodeIdPredicate(UUID nodeId) {
        this.nodeId = nodeId;
    }

    /** {@inheritDoc} */
    @Override public boolean apply(ClusterNode e) {
        return e.id().equals(nodeId);
    }

    /** {@inheritDoc} */
    @Override public String toString() {
        return S.toString(EqualsClusterNodeIdPredicate.class, this);
    }
}
