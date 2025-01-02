library(magrittr)
library(DESeq2)

args <- commandArgs(trailingOnly = TRUE)

cancer <- args[1]
opts <- args[2]
meta <- args[3]


dirs <- '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/Count_/'

metaInfo <- read.table(meta, header = T, sep = '\t')
metaInfo$Group <- factor(metaInfo$Group,levels = c('Tumor', 'Normal'))
# metaInfo$DataBase <- factor(metaInfo$DataBase,levels = c('TCGA', 'GTEx'))

print(paste0('Get metaInfo of ', cancer))
metaSub <- metaInfo[metaInfo$Cancer == cancer,]
rownames(metaSub) <- metaSub$Sample
metaSub$Sample <- NULL


countData <- read.table(paste0(dirs, cancer, '.txt'), header = T, row.names = 1, sep = '\t', check.names = F) %>% as.matrix()
countData <- countData[grep('ENSG', x = rownames(countData)),]
metaSub <- metaSub[match(colnames(countData), rownames(metaSub)),]

if (length(unique(metaSub$DataBase)) == 1) {
    design = ~ Group
} else {
    design = ~ DataBase + Group
}

print(paste0('Formula: ', design))
dds <- DESeqDataSetFromMatrix(countData = countData, colData = metaSub, design = design)

smallestGroupSize <- .5
keep <- rowSums(counts(dds) > 0) / ncol(countData) >= smallestGroupSize
dds <- dds[keep,]

dds$Group <- relevel(dds$Group, ref = 'Normal')

dds <- DESeq(dds, parallel = F)
res <- results(dds, contrast=c("Group","Tumor","Normal"), pAdjustMethod = 'fdr', parallel = F, tidy = T)
colnames(res)[1] <- 'EnsembleID'

res$Cancer <- cancer
readr::write_tsv(res, file = paste0(opts, '/', cancer, '.txt'), col_names = T)