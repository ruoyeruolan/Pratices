library(magrittr)
library(DESeq2)

args <- commandArgs(trailingOnly = TRUE)
cancer <- args[1]
# print(cancer)
print(paste0('Processing ', cancer, '...'))
metaInfo <- read.table('/public/workspace/ryrl/FK/TCGA/RNA-seq/Meta/metaSub.txt', header = T, sep = '\t')
dirs <- '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/'
metaSub <- metaInfo  # [metaInfo$Cancer == cancer,]
rownames(metaSub) <- metaSub$Sample
metaSub$Sample <- NULL
metaSub$Group_ <- ifelse(metaSub$Cancer == cancer, yes = cancer, no = 'Others')
metaSub$Group_ <- factor(x = metaSub$Group_, levels = c(cancer, 'Others'))

countData <- read.table(
    '/public/workspace/ryrl/projects/classmates/ryrl/Cancers/TCGA/intermediate/Counts.txt',
    header = T, row.names = 1, sep = '\t', check.names = F) %>% as.matrix()
countData <- countData[grep('ENSG', x = rownames(countData)),]

dds <- DESeqDataSetFromMatrix(
    countData = countData,
    colData = metaSub,
    design = ~ Group_ # ~ DataBase + Group
    # tidy = T
)

smallestGroupSize <- .5
keep <- rowSums(counts(dds) > 0) / ncol(countData) >= smallestGroupSize
dds <- dds[keep,]

dds <- DESeq(dds)

print(paste0('Saving ', cancer, '...')
saveRDS(dds, file = paste0(dirs, 'intermediate/dds_', cancer, '.rds'))
