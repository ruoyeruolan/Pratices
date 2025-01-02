"""
@Introduce  : 
@File       : pydeseq2.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2024/12/20 23:32
"""
import os
import subprocess
import pandas as pd
import multiprocessing as mp

from typing import Union, Optional

class DES:

    def __init__(self, dirs: str = None, opts: str = None, meta: str = None, script: str = None,
                 sep: str ='\t', header: Union[bool, int] =0, index_col: Union[bool, int] = 0):
        self.dirs = dirs
        # self.fname = fname
        self.opts = opts
        self.script = script
        self.meta = meta

        self.sep = sep
        self.header = header
        self.index_col = index_col

        for i in [self.dirs, self.opts]:
            if not os.path.exists(i):
                os.makedirs(i, exist_ok=True)
    
    def read(self, file: str = None) -> pd.DataFrame:
        return pd.read_csv(file, sep=self.sep, header=self.header, index_col=self.index_col)
    
    def get_meta(self) -> pd.DataFrame:
        return self.read(self.meta)
    
    def get_count(self, fname) -> pd.DataFrame:
        return self.read(file=f'{self.dirs}/{fname}.txt')
    
    def main(self, fname: str) -> str:
        return f'Rscript {self.script} {fname} {self.opts} {self.meta}'

def run(obj: object, fname: str = None) -> None:
    cmd = obj.main(fname)

    try:
        results = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        print(f'Args: {results.args}', 
              f'ReturnCode: {results.returncode}',
              f'Stdout:: {results.stdout}', 
              f'Stderr:{results.stderr}', 
              sep='\n')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
    return None

def demo():
    dirs = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Count_/'

    # cancers = [file.split('.')[0] for file in os.listdir(dirs) if file.endswith('.txt')]
    cancers = 'ACC,BLCA,BRCA,CESC,CHOL,COAD,ESCA,GBM,HNSC,KICH,KIRC,KIRP,LGG,LIHC,LUAD,LUSC,OV,PAAD,PRAD,READ,SARC,SKCM,STAD,STES,TGCT,THCA,THYM,UCEC,UCS'.split(',')
    opts = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/results/TCGAGTEx'
    meta = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Meta/metaInfo.txt'

    script = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/scripts/RNAseq/DESeq2analysis.r' 
    obj = DES(dirs=dirs, opts=opts, meta=meta, script=script)
    run(obj, cancers[0])
    return None

def main():
    dirs = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Count_/'
    # cancers = [file.split('.')[0] for file in os.listdir(dirs) if file.endswith('.txt')]
    cancers = 'ACC,BLCA,BRCA,CESC,CHOL,COAD,ESCA,GBM,HNSC,KICH,KIRC,KIRP,LGG,LIHC,LUAD,LUSC,OV,PAAD,PRAD,READ,SARC,SKCM,STAD,STES,TGCT,THCA,THYM,UCEC,UCS'.split(',')
    opts = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/results/TCGAGTEx'
    meta = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Meta/metaInfo.txt'

    script = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/scripts/RNAseq/DESeq2analysis.r'

    obj = DES(dirs=dirs, opts=opts, meta=meta, script=script)
    
    pool = mp.Pool(processes=15)
    for cancer in cancers:
        try:
            if not os.path.exists(f'{opts}/{cancer}.txt'):
                print(f'Processing {cancer}...')
                pool.apply_async(run, args=(obj, cancer))
            else:
                print(f'{cancer} has been processed...')
        except Exception as e:
            print(f'Error: {e} in {cancer}')
    pool.close()
    pool.join()
    return None


if __name__ == '__main__':
    # main()
    demo()
