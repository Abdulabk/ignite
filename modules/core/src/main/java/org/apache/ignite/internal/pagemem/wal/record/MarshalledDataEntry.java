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

package org.apache.ignite.internal.pagemem.wal.record;

import org.apache.ignite.internal.processors.cache.CacheObject;

/**
 * Interface for Data Entry record that was not converted to key, value pair during record deserialization.
 */
public interface MarshalledDataEntry {
    /**
     * @return Data Entry Key type code. See {@link CacheObject} for built-in value type codes.
     */
    byte getKeyType();

    /**
     * @return Key value bytes.
     */
    byte[] getKeyBytes();

    /**
     * @return Data Entry Value type code. See {@link CacheObject} for built-in value type codes.
     */
    byte getValType();

    /**
     * @return Value value bytes.
     */
    byte[] getValBytes();
}
