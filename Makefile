
datasets/itwiki.revision_sample.100k_article_size-changing.tsv:
	wget http://quarry.wmflabs.org/run/75140/output/0/tsv?download=true -qO- > \
	datasets/itwiki.revision_sample.100k_article_size-changing.tsv

datasets/enwiki.labeled_edittypes.w_cache.json: \
	datasets/edit_intention_dataset.json
	cat $< | \
	revscoring extract \
	edittypes.feature_lists.edittypes.edittypes \
	--host=https://en.wikipedia.org/ \
	--input=datasets/edit_intention_dataset.json > $@
