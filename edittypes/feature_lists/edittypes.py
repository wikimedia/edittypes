from revscoring import Feature
from revscoring.features import wikitext
from revscoring.datasources import revision_oriented as ro
from revscoring.datasources.meta import vectorizers
from revscoring.features.meta import aggregators
from revscoring.languages import english

from datasources.diff import (relocation_segments_context, added_segments_context, removed_segments_context)
from wiki_edit_util import (spell_error, stem_overlap, user_history,
                            comment_revert, comment_typo, is_registered,
                            gender_type, segment_length, segment_search_external,
                            segment_search_file, segment_template,
                            segment_reference, segment_internal,
                            segment_external, segment_file, segment_markup,
                            operation_in_template, operation_in_reference,
                            operation_in_internal, operation_in_external,
                            operation_in_file, is_template, is_reference,
                            is_internal, is_external, is_markup, is_file)

revision_features = [	
    ro.revision.page.namespace.id,	
    ro.revision.minor,
    ro.revision.byte_len, 

    ## char features
    wikitext.revision.diff.uppercase_words_added,
    wikitext.revision.diff.chars_added,
    wikitext.revision.diff.chars_removed,
    wikitext.revision.diff.numeric_chars_added,
    wikitext.revision.diff.numeric_chars_removed,
    wikitext.revision.diff.whitespace_chars_added,
    wikitext.revision.diff.whitespace_chars_removed,
    wikitext.revision.diff.markup_chars_added,
    wikitext.revision.diff.markup_chars_removed,
    wikitext.revision.diff.cjk_chars_added,
    wikitext.revision.diff.cjk_chars_removed,
    wikitext.revision.diff.entity_chars_added,
    wikitext.revision.diff.entity_chars_removed,
    wikitext.revision.diff.url_chars_added,
    wikitext.revision.diff.url_chars_removed,
    wikitext.revision.diff.word_chars_added,
    wikitext.revision.diff.word_chars_removed,
    wikitext.revision.diff.uppercase_words_added,
    wikitext.revision.diff.uppercase_words_removed,
    wikitext.revision.diff.punctuation_chars_added,
    wikitext.revision.diff.punctuation_chars_removed,
    ## token features
    wikitext.revision.diff.token_delta_sum,
    wikitext.revision.diff.token_delta_increase,
    wikitext.revision.diff.token_delta_decrease,
    wikitext.revision.diff.token_prop_delta_sum,
    wikitext.revision.diff.token_prop_delta_increase,
    wikitext.revision.diff.token_prop_delta_decrease,
    wikitext.revision.diff.number_delta_sum,
    wikitext.revision.diff.number_delta_increase,
    wikitext.revision.diff.number_delta_decrease,
    wikitext.revision.diff.number_prop_delta_sum,
    wikitext.revision.diff.number_prop_delta_increase,
    wikitext.revision.diff.number_prop_delta_decrease,
    wikitext.revision.diff.whitespace_delta_sum,
    wikitext.revision.diff.whitespace_delta_increase,
    wikitext.revision.diff.whitespace_delta_decrease,
    wikitext.revision.diff.whitespace_prop_delta_sum,
    wikitext.revision.diff.whitespace_prop_delta_increase,
    wikitext.revision.diff.whitespace_prop_delta_decrease,
    wikitext.revision.diff.markup_delta_sum,
    wikitext.revision.diff.markup_delta_increase,
    wikitext.revision.diff.markup_delta_decrease,
    wikitext.revision.diff.markup_prop_delta_sum,
    wikitext.revision.diff.markup_prop_delta_increase,
    wikitext.revision.diff.markup_prop_delta_decrease,
    wikitext.revision.diff.cjk_delta_sum,
    wikitext.revision.diff.cjk_delta_increase,
    wikitext.revision.diff.cjk_delta_decrease,
    wikitext.revision.diff.cjk_prop_delta_sum,
    wikitext.revision.diff.cjk_prop_delta_increase,
    wikitext.revision.diff.cjk_prop_delta_decrease,
    wikitext.revision.diff.entity_delta_sum,
    wikitext.revision.diff.entity_delta_increase,
    wikitext.revision.diff.entity_delta_decrease,
    wikitext.revision.diff.entity_prop_delta_sum,
    wikitext.revision.diff.entity_prop_delta_increase,
    wikitext.revision.diff.entity_prop_delta_decrease,
    wikitext.revision.diff.url_delta_sum,
    wikitext.revision.diff.url_delta_increase,
    wikitext.revision.diff.url_delta_decrease,
    wikitext.revision.diff.url_prop_delta_sum,
    wikitext.revision.diff.url_prop_delta_increase,
    wikitext.revision.diff.url_prop_delta_decrease,
    wikitext.revision.diff.word_delta_sum,
    wikitext.revision.diff.word_delta_increase,
    wikitext.revision.diff.word_delta_decrease,
    wikitext.revision.diff.word_prop_delta_sum,
    wikitext.revision.diff.word_prop_delta_increase,
    wikitext.revision.diff.word_prop_delta_decrease,
    wikitext.revision.diff.uppercase_word_delta_sum,
    wikitext.revision.diff.uppercase_word_delta_increase,
    wikitext.revision.diff.uppercase_word_delta_decrease,
    wikitext.revision.diff.uppercase_word_prop_delta_sum,
    wikitext.revision.diff.uppercase_word_prop_delta_increase,
    wikitext.revision.diff.uppercase_word_prop_delta_decrease,
    wikitext.revision.diff.punctuation_delta_sum,
    wikitext.revision.diff.punctuation_delta_increase,
    wikitext.revision.diff.punctuation_delta_decrease,
    wikitext.revision.diff.punctuation_prop_delta_sum,
    wikitext.revision.diff.punctuation_prop_delta_increase,
    wikitext.revision.diff.punctuation_prop_delta_decrease,
    wikitext.revision.diff.break_delta_sum,
    wikitext.revision.diff.break_delta_increase,
    wikitext.revision.diff.break_delta_decrease,
    wikitext.revision.diff.break_prop_delta_sum,
    wikitext.revision.diff.break_prop_delta_increase,
    wikitext.revision.diff.break_prop_delta_decrease,
    ## token edit features
    wikitext.revision.diff.segments_added,
    wikitext.revision.diff.segments_removed,
    wikitext.revision.diff.tokens_added,
    wikitext.revision.diff.tokens_removed,
    wikitext.revision.diff.numbers_added,
    wikitext.revision.diff.numbers_removed,
    wikitext.revision.diff.markups_added,
    wikitext.revision.diff.markups_removed,
    wikitext.revision.diff.whitespaces_added,
    wikitext.revision.diff.whitespaces_removed,
    wikitext.revision.diff.cjks_added,
    wikitext.revision.diff.cjks_removed,
    wikitext.revision.diff.entities_added,
    wikitext.revision.diff.entities_removed,
    wikitext.revision.diff.urls_added,
    wikitext.revision.diff.urls_removed,
    wikitext.revision.diff.words_added,
    wikitext.revision.diff.words_removed,
    wikitext.revision.diff.uppercase_words_added,
    wikitext.revision.diff.uppercase_words_removed,
    wikitext.revision.diff.punctuations_added,
    wikitext.revision.diff.punctuations_removed,
    wikitext.revision.diff.breaks_added,
    wikitext.revision.diff.breaks_removed,
    wikitext.revision.diff.longest_token_added,
    wikitext.revision.diff.longest_uppercase_word_added,

    # *** language features 
    # *** stop word features 
    english.stopwords.revision.diff.stopwords_added,
    english.stopwords.revision.diff.stopwords_removed,
    english.stopwords.revision.diff.non_stopwords_added,
    english.stopwords.revision.diff.non_stopwords_removed,
    english.stopwords.revision.diff.stopword_delta_sum,
    english.stopwords.revision.diff.stopword_delta_increase,
    english.stopwords.revision.diff.stopword_delta_decrease,
    english.stopwords.revision.diff.non_stopword_delta_sum,
    english.stopwords.revision.diff.non_stopword_delta_increase,
    english.stopwords.revision.diff.non_stopword_delta_decrease,
    english.stopwords.revision.diff.stopword_prop_delta_sum,
    english.stopwords.revision.diff.stopword_prop_delta_increase,
    english.stopwords.revision.diff.stopword_prop_delta_decrease,
    english.stopwords.revision.diff.non_stopword_prop_delta_sum,
    english.stopwords.revision.diff.non_stopword_prop_delta_increase,
    english.stopwords.revision.diff.non_stopword_prop_delta_decrease,

    # *** stemmed features 
    english.stemmed.revision.diff.stem_delta_sum,
    english.stemmed.revision.diff.stem_delta_increase,
    english.stemmed.revision.diff.stem_delta_decrease,
    english.stemmed.revision.diff.stem_prop_delta_sum,
    english.stemmed.revision.diff.stem_prop_delta_increase,
    english.stemmed.revision.diff.stem_prop_delta_decrease,

    # *** badwords 
    english.badwords.revision.diff.matches_added,
    english.badwords.revision.diff.matches_removed,
    english.badwords.revision.diff.match_delta_sum,
    english.badwords.revision.diff.match_delta_increase,
    english.badwords.revision.diff.match_delta_decrease,
    english.badwords.revision.diff.match_prop_delta_sum,
    english.badwords.revision.diff.match_prop_delta_increase,
    english.badwords.revision.diff.match_prop_delta_decrease,

    # *** informals
    english.informals.revision.diff.matches_added,
    english.informals.revision.diff.matches_removed,
    english.informals.revision.diff.match_delta_sum,
    english.informals.revision.diff.match_delta_increase,
    english.informals.revision.diff.match_delta_decrease,
    english.informals.revision.diff.match_prop_delta_sum,
    english.informals.revision.diff.match_prop_delta_increase,
    english.informals.revision.diff.match_prop_delta_decrease
]

feature_spell_error_segment_added = Feature(
    "spell_error_segment_added",
    spell_error,
    depends_on=[wikitext.revision.diff.datasources.segments_added],
    returns=float
)

feature_spell_error_segment_removed = Feature(
    "spell_error_segment_removed",
    spell_error,
    depends_on=[wikitext.revision.diff.datasources.segments_removed],
    returns=float
)

feature_stem_overlap_segments = Feature(
    "stem_overlap_segments",
    stem_overlap,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                wikitext.revision.diff.datasources.segments_removed]
)

feature_user_history = Feature(
    "user_history_registration",
    user_history,
    depends_on=[ro.revision.timestamp,
                ro.revision.user.info.registration]
)

feature_comment_revert = Feature(
    "comment_revert",
    comment_revert,
    depends_on=[ro.revision.comment]
)

feature_comment_length = aggregators.len(
    ro.revision.comment,
    name="comment_length"
)

feature_comment_typo = Feature(
    "comment_typo",
    comment_typo,
    depends_on=[ro.revision.comment]
)

feature_reloc_len = aggregators.len(
    relocation_segments_context,
    name="relocation_length"
)

feature_is_registered = Feature(
    "is_registered",
    is_registered,
    depends_on=[ro.revision.user.info.registration]
)

feature_gender_type = Feature(
    "gender_type",
    gender_type,
    depends_on=[ro.revision.user.info.gender]
)

feature_segment_length_added = Feature(
    "segment_length_added",
    segment_length,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_length_removed = Feature(
    "segment_length_removed",
    segment_length,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_search_external_added = Feature(
    "segment_search_external_added",
    segment_search_external,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)

feature_segment_search_external_removed = Feature(
    "segment_search_external_removed",
    segment_search_external,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_search_file_added = Feature(
    "segment_search_file_added",
    segment_search_file,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_search_file_removed = Feature(
    "segment_search_file_removed",
    segment_search_file,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_template_added = Feature(
    "segment_template_added",
    segment_template,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_template_removed = Feature(
    "segment_template_removed",
    segment_template,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_reference_added = Feature(
    "segment_reference_added",
    segment_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_reference_removed = Feature(
    "segment_reference_removed",
    segment_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_internal_added = Feature(
    "segment_internal_added",
    segment_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_internal_removed = Feature(
    "segment_internal_removed",
    segment_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_external_added = Feature(
    "segment_external_added",
    segment_external,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_external_removed = Feature(
    "segment_external_removed",
    segment_external,
    depends_on=[wikitext.revision.diff.datasources.segments_removed]
)

feature_segment_file_added = Feature(
    "segment_file_added",
    segment_file,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_file_removed = Feature(
    "segment_file_removed",
    segment_file,
    depends_on=[wikitext.revision.diff.datasources.segments_removed])

feature_segment_markup_added = Feature(
    "segment_markup_added",
    segment_markup,
    depends_on=[wikitext.revision.diff.datasources.segments_added]
)
feature_segment_markup_removed = Feature(
    "segment_markup_removed",
    segment_markup,
    depends_on=[wikitext.revision.diff.datasources.segments_removed])

feature_operation_in_template_added = Feature(
    "operation_in_template_added",
    operation_in_template,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_operation_in_template_removed = Feature(
    "operation_in_template_removed",
    operation_in_template,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_operation_in_reference_added = Feature(
    "operation_in_reference_added",
    operation_in_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_operation_in_reference_removed = Feature(
    "operation_in_reference_removed",
    operation_in_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_operation_in_internal_added = Feature(
    "operation_in_internal_added",
    operation_in_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_operation_in_internal_removed = Feature(
    "operation_in_internal_removed",
    operation_in_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_operation_in_external_added = Feature(
    "operation_in_external_added",
    operation_in_external,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_operation_in_external_removed = Feature(
    "operation_in_external_removed",
    operation_in_external,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_operation_in_file_added = Feature(
    "operation_in_file_added",
    operation_in_file,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_operation_in_file_removed = Feature(
    "operation_in_file_removed",
    operation_in_file,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_template_added = Feature(
    "is_template_added",
    is_template,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_template_removed = Feature(
    "is_template_removed",
    is_template,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_reference_added = Feature(
    "is_reference_added",
    is_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_reference_removed = Feature(
    "is_reference_removed",
    is_reference,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_internal_added = Feature(
    "is_internal_added",
    is_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_internal_removed = Feature(
    "is_internal_removed",
    is_internal,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_external_added = Feature(
    "is_external_added",
    is_external,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_external_removed = Feature(
    "is_external_removed",
    is_external,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_markup_added = Feature(
    "is_markup_added",
    is_markup,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_markup_removed = Feature(
    "is_markup_removed",
    is_markup,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

feature_is_file_added = Feature(
    "is_file_added",
    is_file,
    depends_on=[wikitext.revision.diff.datasources.segments_added,
                added_segments_context]
)
feature_is_file_removed = Feature(
    "is_file_removed",
    is_file,
    depends_on=[wikitext.revision.diff.datasources.segments_removed,
                removed_segments_context]
)

text_features = [
    feature_spell_error_segment_added,
    feature_spell_error_segment_removed,
    feature_stem_overlap_segments,
    feature_user_history,
    feature_comment_revert,
    feature_comment_length,
    feature_comment_typo,
    feature_reloc_len,
    feature_is_registered,
    feature_gender_type,
    feature_segment_length_added,
    feature_segment_length_removed,
    feature_segment_search_external_added,
    feature_segment_search_external_removed,
    feature_segment_search_file_added,
    feature_segment_search_file_removed,
    feature_segment_template_added,
    feature_segment_template_removed,
    feature_segment_reference_added,
    feature_segment_reference_removed,
    feature_segment_internal_added,
    feature_segment_internal_removed,
    feature_segment_external_added,
    feature_segment_external_removed,
    feature_segment_file_added,
    feature_segment_file_removed,
    feature_segment_markup_added,
    feature_segment_markup_removed,
    feature_operation_in_template_added,
    feature_operation_in_template_removed,
    feature_operation_in_reference_added,
    feature_operation_in_reference_removed,
    feature_operation_in_internal_added,
    feature_operation_in_internal_removed,
    feature_operation_in_external_added,
    feature_operation_in_external_removed,
    feature_operation_in_file_added,
    feature_operation_in_file_removed,
    feature_is_template_added,
    feature_is_template_removed,
    feature_is_reference_added,
    feature_is_reference_removed,
    feature_is_internal_added,
    feature_is_internal_removed,
    feature_is_external_added,
    feature_is_external_removed,
    feature_is_markup_added,
    feature_is_markup_removed,
    feature_is_file_added,
    feature_is_file_removed
]

edittypes = revision_features + text_features
