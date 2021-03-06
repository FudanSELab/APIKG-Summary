from sekg.ir.doc.wrapper import MultiFieldDocumentCollection, PreprocessMultiFieldDocumentCollection
from sekg.ir.preprocessor.code_text import CodeDocPreprocessor
from sekg.util.annotation import catch_exception

from util.path_util import PathUtil


@catch_exception
def build_doc(pro_name, version):
    input_doc_collection_path = PathUtil.doc(pro_name=pro_name, version=version)
    output_pre_doc_collection_path = PathUtil.pre_doc(pro_name=pro_name, version=version, pre_way="code-pre")
    doc_collection: MultiFieldDocumentCollection = MultiFieldDocumentCollection.load(input_doc_collection_path)
    precess_doc_collection = PreprocessMultiFieldDocumentCollection.create_from_doc_collection(
        preprocessor=CodeDocPreprocessor(), doc_collection=doc_collection)
    precess_doc_collection.save(output_pre_doc_collection_path)


if __name__ == '__main__':
    pro_list = ["jdk8"]
    versions = ["v3"]

    for pro_name in pro_list:
        for version in versions:
            build_doc(pro_name, version)
