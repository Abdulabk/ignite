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

package org.apache.ignite.internal.pagemem.wal.record.delta;

import org.apache.ignite.IgniteCheckedException;
import org.apache.ignite.internal.pagemem.PageMemory;
import org.apache.ignite.internal.processors.cache.persistence.tree.io.DataPageIO;
import org.apache.ignite.internal.processors.cache.persistence.tree.io.PageIO;
import org.apache.ignite.internal.util.typedef.internal.S;

/**
 * MVCC update tx state hint record.
 */
public class DataPageMvccUpdateNewTxStateHintRecord extends PageDeltaRecord {
    /** */
    private int itemId;

    /** */
    private byte txState;

    /**
     * @param grpId Cache group ID.
     * @param pageId Page ID.
     * @param itemId Item id.
     * @param txState Tx state hint.
     */
    public DataPageMvccUpdateNewTxStateHintRecord(int grpId, long pageId, int itemId, byte txState) {
        super(grpId, pageId);

        this.itemId = itemId;
        this.txState = txState;
    }

    /** {@inheritDoc} */
    @Override public void applyDelta(PageMemory pageMem, long pageAddr) throws IgniteCheckedException {
        DataPageIO io = PageIO.getPageIO(pageAddr);

        io.updateNewTxState(pageAddr, itemId, pageMem.realPageSize(groupId()), txState);
    }

    /** {@inheritDoc} */
    @Override public RecordType type() {
        return RecordType.MVCC_DATA_PAGE_NEW_TX_STATE_HINT_UPDATED_RECORD;
    }

    /**
     * @return Item id.
     */
    public int itemId() {
        return itemId;
    }

    /**
     * @return Tx state hint.
     */
    public byte txState() {
        return txState;
    }

    /** {@inheritDoc} */
    @Override public String toString() {
        return S.toString(DataPageMvccUpdateNewTxStateHintRecord.class, this, "super", super.toString());
    }
}
