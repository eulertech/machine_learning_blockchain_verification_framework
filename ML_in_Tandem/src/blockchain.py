'''
framework:
1. function build_model_chain (f0,f1,f2,f3,f4)
2. get_parent() # method
3. get_transaction(n) # method
4. get_total_transaction() # method
5. print_chain()
6. get_first_chain()
7. get_last_chain()
8. compare_two_chain(chain obj)

Author: Liang Kuang
Date: 2019-01-11
'''
import os
import hashlib
import datetime

class block():
    def __init__(self, index, timestamp, data, previous_block):
        # initialize with a empty or loaded chain object
        # chain is a blockchain class object
        self.author = 'liang kuang'
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_block = previous_block
        self.hash = self.hash_block()

    def hash_block(self):
        md5 = hashlib.md5()
        if self.previous_block is not None:
            md5.update(str(self.index).encode() +
                      # str(self.timestamp).encode() +
                       str(self.data).encode() +
                       str(self.previous_block.hash).encode()
                       )
        else: # for the first block. No usage of previous block value
            md5.update(str(self.index).encode() +
                      # str(self.timestamp).encode() +
                       str(self.data).encode() +
                       str("First Genesis Block.").encode()
                       )
        return md5.hexdigest()

    def get_block_length(self):
        '''
        :return:
        '''
        if self.hash is None:
            print("Nothing in this block")
            return None
        else:
            cnt = 1  # TODO: should be 0 or 1
            previousBlock = self.previous_block
            while previousBlock is not None:
                try:
                    previousBlock = previousBlock.previous_block
                except NameError:
                    previousBlock = None
                    continue
                cnt = cnt + 1
            return cnt

    def get_first_block(self):
        parent = self.previous_block
        temp = parent
        while parent is not None:
            temp = parent
            try:
                parent = parent.previous_block
            except NameError:
                parent = None
                continue
        return temp

    def get_last_block(self):
        return self

    def get_nth_block(self, n=1):
        # by default will get the first
        cnt = self.get_block_length()
        if n == cnt:
            return self.get_last_block()
        if n > cnt:
            return None
        else:
            tempBlock = self.previous_block
            while tempBlock is not None:
                cnt = cnt - 1
                if cnt == n:
                    return tempBlock
                else:
                    tempBlock = tempBlock.previous_block
        return None

    def get_previous_block(self):
        return self.previous_block

    def print(self):
        print("print block from end to beginning.")
        print("The last block is: %s with index of %d\n"%(self.hash, self.index))
        previousBlock = self.previous_block
        while previousBlock is not None:
            print("The previous block is: %s with index of %d\n"%(previousBlock.hash, previousBlock.index))
            previousBlock = previousBlock.previous_block

    def save(self, filename):
        '''
        save block chain object to file storage
        :param filename: the location of file to be saved
        :return: Nothing
        '''
        try:
            with open(filename, 'w') as f:
                f.write(self)
        except IOError:
            return -1

    def load(self, filename):
        '''
        Load a saved blockchain object
        :param filename: The file path of blockchain
        :return:  the blockchain object
        '''
        if not os.path.isfile(filename):
            raise IOError(FileNotFoundError)
        else:
            with open(filename, 'r') as f:
                block = f.read()
            return block


def md5sum(filename, blocksize = 65536):
    import hashlib
    hash=hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

import datetime
def create_genesis_block(index, timestamp=datetime.datetime.now(), data="Genesis block", previous_block = None ):
    from blockchain import block
    return block(0, timestamp, data, previous_block)


def create_next_block(data, last_block):
    from blockchain import block
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = data
    previous_block = last_block
    return block(this_index, this_timestamp, this_data, previous_block)

def compare_model_chains(chain1, chain2):
    '''
    :param chain1: blockchain one
    :param chain2: blockchain two
    :return: True if two chain the same
    '''
    # compare the length
    # compare the first and last hash
    assert type(chain1) == type(chain2), "The two types are different. Exit(1)"
    len1 = chain1.get_block_length()
    len2 = chain2.get_block_length()
    last_block1 = chain1.get_last_block().hash
    last_block2 = chain2.get_last_block().hash

    if len1 == len2 and last_block1 == last_block2:
        return True
    else:
        return False

def compare_nth_block(chain1, chain2, n):
    '''
    :param chain1: A blockchain object
    :param chain2: A blockchain object
    :param n: The nth block from parent
    :return: True of False
    '''
    # compare the nth block starting from parent
    assert type(chain1) == type(chain2), "The two types are different. Exit(1)"
    n_block1 = chain1.get_nth_block(n)
    n_block2 = chain2.get_nth_block(n)
    if n_block1 == n_block2:
        return True
    else:
        return False

def file_as_bytes(file):
    while file:
        return file.read()

def build_model_chain(list_of_files):
    # TODO: need to add the capability of build chain with list of list. Say a step can contains multiple files. recursively update them for that step.
    '''
    :param list_of_files: list of files from genesis to the end block
    :return: a blockchain object
    '''
    from blockchain import file_as_bytes
    from blockchain import create_genesis_block
    import datetime

    if len(list_of_files) == 0:
        raise ValueError("The list of files must not be empty")
    else:
        for i in range(len(list_of_files)):
            if i == 0:
                index = i
                timestamp = datetime.datetime.now()
                data = file_as_bytes(open(list_of_files[i],'rb')) # it will change image file (png,jpeg etc) data with rb on windows
                model_chain = create_genesis_block(0, timestamp, data)
                model_chain.print()
            else:
                index = i
                data = file_as_bytes(open(list_of_files[i],'rb'))
                timestamp = datetime.datetime.now()
                model_chain = create_next_block(data, model_chain)
                model_chain.print()
    return model_chain
# unit test

if __name__ == "__main__":

    from blockchain import create_genesis_block
    from blockchain import create_next_block
    from blockchain import compare_model_chains
    from blockchain import compare_nth_block

    blockChain = [create_genesis_block(0)]
    previous_block = blockChain[0]
    print(type(previous_block))

    num_blocks = 10
    for i in range(0, num_blocks):
        data = "Creating block" + str(i)
        block2add = create_next_block(data, last_block=previous_block)
        blockChain.append(block2add)
        previous_block = block2add

        print("Block %d has been added to the blockChain \n", block2add.index)
        print("Hash: %s\n", block2add.hash)

    last_block = blockChain[-1]
    print("Last block's index is %d"%last_block.index)
    # test the functions
    n = 2
    print('The first block is: %s with index of %d'%(last_block.get_first_block().hash, last_block.get_first_block().index))
    print('The last block is: %s with index of %d'%(last_block.get_last_block().hash, last_block.get_last_block().index))
    print('The length of this block process is %d'%last_block.get_block_length())
    print('The index of this block is %d'%last_block.index)
    print('The %d th block is: %s'%(n,last_block.get_nth_block(n).hash))
    print('Previous block is: %s with index of %d' %(last_block.get_previous_block(), last_block.get_previous_block().index))
    print('Compare last and previous chain %s'%str(compare_model_chains(last_block, last_block.previous_block)))
    chain2 = last_block
    chain3 = last_block.previous_block
    print('Compare first block %s'%str(compare_nth_block(chain2,chain3,1)))
    print('Compare 2nd block %s'%str(compare_nth_block(chain2,chain3,2)))
