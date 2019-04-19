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

package org.apache.ignite.internal.visor.query;

import java.util.Map;
import java.util.UUID;
import org.apache.ignite.internal.processors.query.GridQueryCancel;
import org.apache.ignite.internal.processors.task.GridInternal;
import org.apache.ignite.internal.processors.task.GridVisorManagementTask;
import org.apache.ignite.internal.util.typedef.internal.S;
import org.apache.ignite.internal.visor.VisorEither;
import org.apache.ignite.internal.visor.VisorJob;
import org.apache.ignite.internal.visor.VisorOneNodeTask;
import org.apache.ignite.internal.visor.util.VisorExceptionWrapper;

import static org.apache.ignite.internal.visor.query.VisorQueryUtils.scheduleQueryStart;

/**
 * Task for execute SQL fields query and get first page of results.
 */
@GridInternal
@GridVisorManagementTask
public class VisorQueryTask extends VisorOneNodeTask<VisorQueryTaskArg, VisorEither<VisorQueryResult>> {
    /** */
    private static final long serialVersionUID = 0L;

    /** {@inheritDoc} */
    @Override protected VisorQueryJob job(VisorQueryTaskArg arg) {
        return new VisorQueryJob(arg, debug);
    }

    /**
     * Job for execute SCAN or SQL query and get first page of results.
     */
    private static class VisorQueryJob extends VisorJob<VisorQueryTaskArg, VisorEither<VisorQueryResult>> {
        /** */
        private static final long serialVersionUID = 0L;

        /**
         * Create job with specified argument.
         *
         * @param arg Job argument.
         * @param debug Debug flag.
         */
        private VisorQueryJob(VisorQueryTaskArg arg, boolean debug) {
            super(arg, debug);
        }

        /** {@inheritDoc} */
        @Override protected VisorEither<VisorQueryResult> run(final VisorQueryTaskArg arg) {
            try {
                UUID nid = ignite.localNode().id();

                GridQueryCancel cancel = new GridQueryCancel();

                Map<String, VisorQueryHolder> storage = ignite.cluster().nodeLocalMap();

                VisorQueryHolder holder = new VisorQueryHolder(true, null, cancel);

                storage.put(holder.getQueryID(), holder);

                scheduleQueryStart(ignite, holder, arg, cancel);

                return new VisorEither<>(new VisorQueryResult(nid, holder.getQueryID(), null, null, false, 0));
            }
            catch (Throwable e) {
                return new VisorEither<>(new VisorExceptionWrapper(e));
            }
        }

        /** {@inheritDoc} */
        @Override public String toString() {
            return S.toString(VisorQueryJob.class, this);
        }
    }
}
