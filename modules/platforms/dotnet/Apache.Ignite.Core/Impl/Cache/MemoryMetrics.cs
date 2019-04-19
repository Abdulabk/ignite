﻿/*
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

namespace Apache.Ignite.Core.Impl.Cache
{
    using System.Diagnostics;
    using Apache.Ignite.Core.Binary;
    using Apache.Ignite.Core.Cache;

    /// <summary>
    /// Memory metrics.
    /// </summary>
#pragma warning disable 618
    internal class MemoryMetrics : IMemoryMetrics
#pragma warning restore 618
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="MemoryMetrics"/> class.
        /// </summary>
        public MemoryMetrics(IBinaryRawReader reader)
        {
            Debug.Assert(reader != null);

            Name = reader.ReadString();
            TotalAllocatedPages = reader.ReadLong();
            AllocationRate = reader.ReadFloat();
            EvictionRate = reader.ReadFloat();
            LargeEntriesPagesPercentage = reader.ReadFloat();
            PageFillFactor = reader.ReadFloat();
        }

        /** <inheritdoc /> */
        public string Name { get; private set; }

        /** <inheritdoc /> */
        public long TotalAllocatedPages { get; private set; }

        /** <inheritdoc /> */
        public float AllocationRate { get; private set; }
        
        /** <inheritdoc /> */
        public float EvictionRate { get; private set; }

        /** <inheritdoc /> */
        public float LargeEntriesPagesPercentage { get; private set; }

        /** <inheritdoc /> */
        public float PageFillFactor { get; private set; }
    }
}
