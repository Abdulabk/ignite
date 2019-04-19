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

package org.apache.ignite.internal.processors.query;

import org.apache.ignite.IgniteException;

/**
 * Behavior options when an attempt to start a nested transaction is made.
 */
public enum NestedTxMode {
    /** Previously started transaction will be committed, new transaction will be started. */
    COMMIT,

    /** Warning will be printed to log, no new transaction will be started. */
    IGNORE,

    /** Exception will be thrown, previously started transaction will be rolled back. */
    ERROR;

    /** Default handling mode. */
    public static final NestedTxMode DEFAULT = ERROR;

    /**
     * Get enum value from int
     *
     * @param val Int value.
     * @return Enum value.
     * @throws IgniteException if the is no enum value associated with the int value.
     */
    public static NestedTxMode fromByte(byte val) {
        switch (val) {
            case 1:
                return COMMIT;

            case 2:
                return IGNORE;

            case 3:
                return ERROR;

            default:
                throw new IgniteException("Invalid nested transactions handling mode: " + val);
        }
    }
}
