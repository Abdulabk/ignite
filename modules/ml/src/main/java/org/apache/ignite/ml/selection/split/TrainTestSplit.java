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

package org.apache.ignite.ml.selection.split;

import java.io.Serializable;
import org.apache.ignite.lang.IgniteBiPredicate;

/**
 * Dataset split that encapsulates train and test subsets.
 *
 * @param <K> Type of a key in {@code upstream} data.
 * @param <V> Type of a value in {@code upstream} data.
 */
public class TrainTestSplit<K, V> implements Serializable {
    /** */
    private static final long serialVersionUID = 2165934349492062372L;

    /** Filter that selects train subset of the dataset. */
    private final IgniteBiPredicate<K, V> trainFilter;

    /** Filter that select test subset of the dataset. */
    private final IgniteBiPredicate<K, V> testFilter;

    /**
     * Constructs a new instance of train test split.
     *
     * @param trainFilter Filter that passes train subset of the dataset.
     * @param testFilter Filter that passes test subset of the dataset.
     */
    public TrainTestSplit(IgniteBiPredicate<K, V> trainFilter, IgniteBiPredicate<K, V> testFilter) {
        this.trainFilter = trainFilter;
        this.testFilter = testFilter;
    }

    /** */
    public IgniteBiPredicate<K, V> getTrainFilter() {
        return trainFilter;
    }

    /** */
    public IgniteBiPredicate<K, V> getTestFilter() {
        return testFilter;
    }
}
