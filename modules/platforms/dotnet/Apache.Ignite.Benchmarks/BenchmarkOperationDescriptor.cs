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

namespace Apache.Ignite.Benchmarks
{
    using System;

    /// <summary>
    /// Benchmark operation descriptor.
    /// </summary>
    internal class BenchmarkOperationDescriptor
    {
        /// <summary>
        /// Create new operation descriptor.
        /// </summary>
        /// <param name="name">Name.</param>
        /// <param name="operation">Operation.</param>
        /// <param name="weight">Weight.</param>
        /// <returns>Operation descriptor.</returns>
        public static BenchmarkOperationDescriptor Create(string name, Action<BenchmarkState> operation, int weight)
        {
            if (string.IsNullOrEmpty(name))
                throw new Exception("Operation name cannot be null or empty.");

            if (operation == null)
                throw new Exception("Operation cannot be null: " + name);

            if (weight <= 0)
                throw new Exception("Operation weight cannot be negative [name=" + name + ", weight=" + weight + ']');

            return new BenchmarkOperationDescriptor
            {
                Name = name,
                Operation = operation,
                Weight = weight
            };
        }

        /// <summary>
        /// Unique operation name.
        /// </summary>
        public string Name { get; private set; }

        /// <summary>
        /// Operation delegate.
        /// </summary>
        public Action<BenchmarkState> Operation { get; private set; }

        /// <summary>
        /// Weight.
        /// </summary>
        public int Weight { get; private set; }
    }
}
