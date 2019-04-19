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

package org.apache.ignite.cache.hibernate;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCheckedException;
import org.hibernate.cache.CacheException;
import org.hibernate.cache.spi.GeneralDataRegion;
import org.hibernate.cache.spi.QueryResultsRegion;
import org.hibernate.cache.spi.TimestampsRegion;
import org.hibernate.engine.spi.SessionImplementor;
import org.jetbrains.annotations.Nullable;

/**
 * Implementation of {@link GeneralDataRegion}. This interface defines common contract for {@link QueryResultsRegion}
 * and {@link TimestampsRegion}.
 */
public class HibernateGeneralDataRegion extends HibernateRegion implements GeneralDataRegion {
    /**
     * @param factory Region factory.
     * @param name Region name.
     * @param ignite Grid.
     * @param cache Region cache.
     */
    HibernateGeneralDataRegion(HibernateRegionFactory factory, String name,
        Ignite ignite, HibernateCacheProxy cache) {
        super(factory, name, ignite, cache);
    }

    /** {@inheritDoc} */
    @Nullable @Override public Object get(SessionImplementor ses, Object key) throws CacheException {
        try {
            return cache.get(key);
        }
        catch (IgniteCheckedException e) {
            throw new CacheException(e);
        }
    }

    /** {@inheritDoc} */
    @Override public void put(SessionImplementor ses, Object key, Object val) throws CacheException {
        try {
            cache.put(key, val);
        }
        catch (IgniteCheckedException e) {
            throw new CacheException(e);
        }
    }

    /** {@inheritDoc} */
    @Override public void evict(Object key) throws CacheException {
        HibernateAccessStrategyAdapter.evict(ignite, cache, key);
    }

    /** {@inheritDoc} */
    @Override public void evictAll() throws CacheException {
        try {
            HibernateAccessStrategyAdapter.evictAll(cache);
        }
        catch (IgniteCheckedException e) {
            throw HibernateRegionFactory.EXCEPTION_CONVERTER.convert(e);
        }
    }
}