import os
import subprocess
import pandas as pd
import multiprocessing as mp


def get_cancer_types(metaInfo: pd.DataFrame) -> list:
    return metaInfo['Cancer'].unique().tolist()


def main(cancer: str) -> None:    
    scripts = '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/scripts/RNAseq/demo.r'
    # os.system(f'Rscript {scripts} {cancers[0]}')
    cmd = f'Rscript {scripts} {cancer}'
    
    try:
        results = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f'Args: {results.args}', f'ReturnCode: {results.returncode}',
            f'Stdout:: {results.stdout}', f'Stderr:{results.stderr}', sep='\n')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
    return None

def run() -> None:
    # print('Processing MetaInfo ...')
    metaInfo = pd.read_csv('/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Meta/metaSub.txt', sep='\t', header=0)
    cancers = get_cancer_types(metaInfo=metaInfo)

    # print('Processing ...')
    # pool = mp.Pool(processes=5)
    for cancer in cancers:
        try:
            print(f'Processing {cancer} ...')
            # pool.apply_async(main, args=(cancer,))
            main(cancer)
        except Exception as e:
            print(f'Error: {e}')
            continue
    # pool.close()
    # pool.join()
    return None
    

if __name__ == '__main__':
    run()
