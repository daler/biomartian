import pytest

import pandas as pd


from biomartian.args.validate_args import validate_args


def describe_validate_args():

    def test_with_valid_args(valid_args):
        validate_args(valid_args)

    def test_with_invalid_args_too_few_intypes(invalid_args_too_few_intypes):
        with pytest.raises(ValueError):
            validate_args(invalid_args_too_few_intypes)

    @pytest.fixture
    def valid_args():
        return {'mergecol': ['0', '0'],
                'intype': ['external_gene_name', 'external_gene_name'],
                'outtype': ['entrezgene', 'refseq_mrna'],}

    @pytest.fixture
    def invalid_args_too_few_intypes():

        return {'mergecol': ['0', '0'],
                'intype': ['external_gene_name'],
                'outtype': ['entrezgene', 'refseq_mrna'],}
