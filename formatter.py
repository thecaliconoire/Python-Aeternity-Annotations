from aeternity.epoch import BlockWithTx, Transaction, AENSClaimTx, AENSPreclaimTx, GenericTx
##NO name errors within AETERNITY.EPOCH BlockWithTx, Transaction, AENSClaimTx, AENSPreclaimTx, GenericTx
def pretty_account(account_hash):
    """Pretty prints (formats) the account hash"""
    return account_hash[:8] + '...' + account_hash[-6:]


def pretty_transaction(tx: Transaction):
    """Pretty prints (formats) the transaction"""
    info = ''
    if type(tx) == GenericTx:
        return tx.tx
    if type(tx.tx) == AENSClaimTx:
        account = pretty_account(tx.tx.account)
        info = f'name: {tx.tx.name} account: {account}'
    elif type(tx.tx) == AENSPreclaimTx:
        account = pretty_account(tx.tx.account)
        info = f'commitment: {tx.tx.commitment} account: {account}'
    return f'TX: {tx.tx.type} {info} {tx.hash}'


def pretty_block(block: BlockWithTx):
    """Pretty prints (formats) the blocks attached to transaction"""
    transactions = '\n    '.join(pretty_transaction(tx) for tx in block.transactions)
    return f'''BLOCK: height {block.height} hash: {block.hash}
transactions:
    {transactions}'''
