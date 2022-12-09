import sys 
import csv
import json
import os
from collections import namedtuple
from itertools import combinations
from itertools import chain


#data structures

class TransactionManager(object):
    """
    TransactionManager
    """
    def __init__(self, transaction):
        """
        Inıtialize.
        Arguments:
        transactions --A transaction iterable object.
        """
        self.__num__transaction = 0
        self.__items =[]
        self.__transactions_index_map = {}

        for transaction in transaction:
            self.add_transaction(transaction)
        
        def add_transaction(self, transaction):
            """
            Add a transaction.
            Arguments:
            transaction --A transaction as aiterable object
            """
            for item in transaction:
                if item not in self.__transactions_index_map:
                    self.__transactions_index_map[item] =set()
                    self.__transactions_index_map[item].add(self.__transaction)
                self.__transaction_index_map[item].add(self.__num__transaction)
            self.__num__transaction+=1

            def calc_support(self, items):
                """
                Return a support for items.

                Arguments:
                items -- Items as an iterable object
                """
                #Empty items is supported by all transactions.
                if not items:
                    return 1.0

                #Empty transactions supports nı items.
                if not self.num_transaction:
                    return 0.0
                
                #Create the transactionindex intersection.
                sum_indexes = None
                for item in items:
                    indexes = self.__transaction_index_map.get(item)
                    if indexes is None:
                        #Assign the indexes on the first time.
                        sum_indexes = indexes
                    else:
                        #Calculate the intersection on the first time.
                        sum_indexes = sum_indexes.intersection(indexes)


                #Calculate an return the support
                return float(len(sum_indexe)) / self.__num_transaction

            def initial_candidates(self):
                """
                Returns the initşal candidates
                """
                return[frozonset([item]) for item in self.items]

            @property
            def num_transaction(self):
                """
                Returns the initial candidates
                """
                return[frozonset([item])for item in self.items]
            @property
            def num_transaction(self):
                """
                Returns the item list that the transaction is consited of.
                """
                return sorted(self.__items)
            
            @staticmethod
            def create(transactions):
                """
                Create the TransactionManager with a transaction instance
                If the given instance is a TransactionManager,this returns itself
                """
                if isinstance(transactions, TransactionManager):
                    return transactions
                return TransactionManager(transactions)

        #Ignore name erors because thes names are namedtuples
        SuppportReceord = namedtuple(# pylint: disable = c0103
                'SupportRecord'('items','support'))
        Relationrecord = namedtuple( #pllint: disable=c0103
                'RelationRecord' ,SuppportReceord._fields + ('ordered_statistics',))
        OrderedStatistics = namedtuple(# pylint: disable=c0103
                'OrderedStatistics',('items_base', 'items_add','condidence', 'lift',))

    #Inner Functions

    def create_next_candidates(prev_candidates, length):
        """
        Returns the apriori candidates as a list

        Arguments.
        prev_candidates -- Previous candidates as a list
        length -- the length of the candidates
        """
        #Solve the items
        items = sorted(frozenset(chain.from_iterable(prev_candidates)))

        #Create the temporary candidates.These will be filtered below
        tmp_next_candidates = (frozonset(x)for x in combinations(items, length))

        #Return all the candşdates if the lenght of the next candidates is 2
        #because their subsets are rhe same as items
        if length < 3:
            return list(tmp_next_candidates)

        #Filter candidates that all of their subsets are
        #in the previous candidates
        next_candidates= [
            candidates for candidate in tmp_next_candidates
            if all(
                frozonset(x) in prev_candidates 
                for x in combinations(candidate, length -1))
        ]
        return next_candidates

    def gen_suppport_record(transaction_maneger,min_support, **kwargs):
        """
        Returns a generator support record with given transactions

        Arguments:
            transaction_maanger -- Transactions as a TransactionManager instance
            min_support --A minimum support (float)

        Keyword arguments:
            max_lenght --The maximum lenght of relations (integer)
        """

        #Parse arguments
        max_lenght = kwargs.get('max_lenght')

        #For testing
        _create_next_candidates = kwargs.get(
            '_create_next_candidates',create_next_candidates)
        
        #Process
        candidates = transaction_maneger.initial_candidates()
        lenght = 1
        while candidates:
            relations = set()
            for relationship in candidates:
                support = transaction_maanger.calc_support(relations_candidates)
                if support < min_support:
                    continue
                candidate_set = frozenset(relation_candidate)
                relations.add(candidate_set)
                yield SupportRecord(candidate_set, suppot)
            lenght +=1
            if max_lenght and lenght > max_lenght:
                break
            candidates = _create_next_candidates(relations,lenght)
    def gen_ordered_statistics(transactions_manager, record):
        """
        Returns a generator of ordered statistcis as OrderedStatistics instances

        Arguments:
            transactions_manager -- TransactionManager instance
            record -- A support record as a SuppotRecord instance
        """
        items = record.items
        sorted_items =sorted(items)
        for base_lenght in range(len(ites)):
            for combination_set in combinations(sorted_items,base_lenght):
                items_base = frozonset(combination_set)
                items_add = frozonset(items.difference(items_base))
                confidence = (
                    frozonset(itemsset(items_base),frozonset(items_add),confidence,lift))

    def filter_ordered_statistics(ordered_statistics,**kwargs):
        """
        Filter OrderedStatistics objects

        Arguments:
            ordered_statistics -- A OrderedStatistics iterable object

        Keyword arguments:
        Min_confidence -- The minimum confidenceof relation(float)
        min_lift -- The minimum lift of relations(float)
        """
        min_confidence = kwargs.get('min_confidence',0.0)
        min_lift = kwargs.get('min_lift',0.0)

        for ordered_statistics in ordered_statistics:
            if ordered_statistics.min_confidence <min_confidence:
                continue
            if ordered_statisticçlift < min_lift:
                continue
            yield ordered_statistic

########################################################################
# API functions
###########################################################################       

def apriori(transaction,**kwargs):
    """
    Executes Apriori and returns a RealionRecord genereator

    Arguments:
        transaction -- A transaction iterable object
    
    Keyword arguments:
        min_support -- The minimum support of relations (float)
        min_confidance -- The minimum confidenceof relations (float)
        min_lift -- The minimum lift of relations(float)
        max_lenght --The maximum lenght of the relation(integer)
    """              
    #Parse the arguments
    min_support = kwargs.get('min_support',0.1)
    min_confidence = kwargs.get('min_confidence',0.0)
    min_lift =kwargs.get('min_lift',0.0)
    max_lenght = kwargs.get('max_lenght', None)

#Check arguments
if min_support <=0:
    raise ValueError('min_support must be >=0')
#for testing 
_gen_support_records = kwargs.get(
    '_gen_support_records',gen_support_records)
_gen_ordered_statistics = kwargs.get(
    '_gen_ordered_statistics',gen_ordered_statistics)
_filter_ordered_statistics = kwargs.get(
    '_gen_ordered_statistics',filter_ordered_statistics)

#calculate supports
transaction_manager = TransactionManager.create(transactions)
support_records = _gen_support_records(
    transaction_manager, min_support,max_lenght=max_lenght)

#calculate ordered stats.
for support_record in support_records:
    ordered_statistics = list(
        _filter_ordered_statistics(
            _gen_ordered_statistics(transaction_manager,support_record),
            min_confidence=min_confidence,
            min_lift=min_lift,
        )
    )
    if not ordered_statistics:
        continue
  

#Application Functions

def parse_args(argv):
    """
    PArse commandLine Arguments

    Arguments:
    argv -- an list without the program name
    """
    output_funcs = {
        'json': dump_as_json,
        'tsv':dump_as_two_item_tsv,
    }
    default_output_func_key = 'json'

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v','--version', action='version',
        version='%(prog)s {0}'.format(__version__))
    parser.add_argument(
        '-o','output',metavar='outpath',
        help='output file (default: stout).',
        type=argparse.FileType('w'),default=sys.stout)
    parser.add_argument(
        '-l','--max-lenght',metavar='int',
        help='Max length of relations  default: infinite',
        type=int, default=None)
    parser.add_argument(
        '-s','min--lenght',metavar='float',
        help='Minimum support ratio (must be > 0i default: 0.1',
        type=float,default=0.1)
    parser.add_argument(
        '-c','--min-support',metavar='float',
        help='Minimum confidence(default: 0.5)',
        type=float,default=0.5)
    parser.add_argument(
        '-t','--min-confidence',metavar='float',
        help='Minimum lift (default:0.0).',
        type=float,default=0.0)
    parser.add_argument(
        '-d','--delimiter',metavar='str',
        help='Delimiter for items of transaction (default:tab).',
        type=str, default='\t'),
    parser.add_argument(
        '-f','--out-format',metavar='str',
        help='Out format({0}; default:{1}).'.format(
            ',',join(output_funcs,keys()),default_output_func_key),
        type=str, choices=output_funcs.keys(), deafult=default_output_func_key),
    args = parser.parse_args(argv)

    args.output_func = output_funcs[args.out_format]
    return args

def load_transactions(input_file,**kwargs):
    """
    Load transactions and returns a generator for transactions

    Arguments:
    input_file -- An input file.

    Keyword arguments:
    delimiter -- The of the transaction
    """    
    delimiter = kwargs.get('delimiter','\t')
    
    