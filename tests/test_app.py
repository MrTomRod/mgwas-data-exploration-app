import os
import shutil
from shutil import copytree
from unittest import TestCase
from mgwas_data_exploration_app.main import mgwas_app

os.environ['MGWAS_LINK_ONLY'] = 'true'
os.chdir('..')


def setup_test(src, dst):
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    copytree(src, dst, ignore_dangling_symlinks=True)


def run_test(test_dir: str, **kwargs):
    setup_test(f'data/{test_dir}', f'out/{test_dir}')
    mgwas_app(
        summary_df=f'out/{test_dir}/summary_orig.tsv',
        traits_df=f'out/{test_dir}/traits_df.tsv',
        app_config=f'out/{test_dir}/app_config.json',
        workdir=f'out/{test_dir}',
        # scores_x_scale='linear',
        **kwargs
    )


class Test(TestCase):
    def test_tetr(self):
        run_test('tetr', is_numeric=False)

    def test_44prop_small(self):
        run_test('44prop-small', is_numeric=False, dendrogram_x_scale='squareroot')

    def test_44prop_small_numeric(self):
        run_test('44prop-small-numeric', is_numeric=True)

    def test_44prop_small_numeric_only(self):
        run_test('44prop-small-numeric-only', is_numeric=True)

    def test_44prop_full(self):
        run_test('44prop-full', is_numeric=False, dendrogram_x_scale='squareroot')

    def test_44prop_full_numeric(self):
        run_test('44prop-full-numeric', is_numeric=True)
