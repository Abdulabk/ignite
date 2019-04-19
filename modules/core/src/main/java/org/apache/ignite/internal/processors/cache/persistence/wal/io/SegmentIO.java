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

package org.apache.ignite.internal.processors.cache.persistence.wal.io;

import org.apache.ignite.internal.processors.cache.persistence.file.FileIO;
import org.apache.ignite.internal.processors.cache.persistence.file.FileIODecorator;

/**
 * Implementation of {@link FileIO} specified for WAL segment file.
 */
public class SegmentIO extends FileIODecorator {
    /** Segment id. */
    private final long segmentId;

    /**
     * @param id Segment id.
     * @param delegate File I/O delegate
     */
    public SegmentIO(long id, FileIO delegate) {
        super(delegate);
        segmentId = id;
    }

    /**
     * @return Segment id.
     */
    public long getSegmentId() {
        return segmentId;
    }
}
