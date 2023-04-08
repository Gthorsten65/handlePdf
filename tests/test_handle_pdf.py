import sys
import datetime

# setting path
sys.path.append('../pdf_splitt')

from handlePdf import HandlePdf
from handlePdf import HandlePdfErrorCode
import logging


class TestHandlePdf():
    def setup(self):
        dbg_lvl_int = 2
        dbg_file_str = 'c:/Development/pdf_splitt/log.txt'
        self.test_obj = HandlePdf(dbg_lvl_int, dbg_file_str)

    def test_set_task_split_parameter(self):
        # def set_task_split_parameter(self, input_file: str, output_file: str, start_page: int, end_page: int):
        input_file = None
        output_file = None
        start_page = 0
        end_page = 0
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_OUTPUTFILE_NOT_SET

        input_file = None
        output_file = "None"
        start_page = 0
        end_page = 0
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_INPUTFILE_NOT_SET

        input_file = "None"
        output_file = "None"
        start_page = None
        end_page = None
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_INPUTFILE_NO_FILE
        print("Hello")

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = None
        end_page = None
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_START_PAGE_NOT_SET

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = 0
        end_page = None
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_END_PAGE_NOT_SET

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = 0
        end_page = 0
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_START_END_PAGE_VALUES

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = 1
        end_page = 0
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_START_END_PAGE_VALUES

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = -1
        end_page = 0
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_START_END_PAGE_VALUES

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = -3
        end_page = -2
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_START_END_PAGE_VALUES

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = 1
        end_page = 2
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        assert error_code == HandlePdfErrorCode.ERROR_NO_ERROR

    def test_set_task_meta_data_parameter(self):
        input_file = None
        output_file = None
        meta_data_str = None
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_OUTPUTFILE_NOT_SET

        input_file = None
        output_file = "None"
        meta_data_str = None
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_INPUTFILE_NOT_SET

        input_file = "None"
        output_file = "None"
        meta_data_str = None
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_INPUTFILE_NO_FILE

        input_file = "../TestDocA.pdf"
        output_file = "None"
        meta_data_str = "Hello"
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_METADATA_INVALID

        meta_data_str = {'/Autho': 'John Doe',
                         '/Keywords': 'Versicherung Allianz, KFZ, KFZ - Versicherung',
                         '/CreationDate': 'D:20221108',
                         '/CreatorTool': 'synOCR 1.022'
                         }

        input_file = "../TestDocA.pdf"
        output_file = "None"
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_PARAM_NOT_A_KNOWN_KEY

        meta_data_str = {'/Author': 'John Doe',
                         '/Keywords': 'Versicherung Allianz, KFZ, KFZ - Versicherung',
                         '/CreationDate': 'D:20221108',
                         '/CreatorTool': 'synOCR 1.022'
                         }

        input_file = "../TestDocA.pdf"
        output_file = "None"
        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == 0

        print("Hello")

    def test_pdf_open(self):
        input_file = "../TestDoc.docx"
        output_file = "None"
        start_page = 1
        end_page = 2
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        error_code = self.test_obj.open_pdf()
        assert error_code == HandlePdfErrorCode.ERROR_INPUTFILE_NOT_READABLE

        input_file = "../TestDocA.pdf"
        output_file = "None"
        start_page = 1
        end_page = 2
        error_code = self.test_obj.set_task_split_parameter(input_file, output_file, start_page, end_page)
        error_code = self.test_obj.open_pdf()
        assert error_code == HandlePdfErrorCode.ERROR_NO_ERROR

    def test_write_metadata(self):
        input_file = "../Test_4_pages_A.pdf"
        output_file = "../Test_4_pages_A2.pdf"

        meta_data_str = "{'/Author': 'John Doe', '/Keywords': 'Versicherung Allianz, KFZ, KFZ - Versicherung', '/CreationDate': 'D:20221108', '/CreatorTool': 'synOCR 1.022' }"

        error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, meta_data_str)
        assert error_code == HandlePdfErrorCode.ERROR_NO_ERROR

        error_code = self.test_obj.open_pdf()
        assert error_code == HandlePdfErrorCode.ERROR_NO_ERROR

        error_code = self.test_obj.write_metadata()

        creator_str = "its me"

        # error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, creator_str)
        # error_code = self.test_obj.open_pdf()

        # self.test_obj._print_metadata()
        # self.test_obj.write_metadata()

        # input_file = "../Test_4_pages_A2.pdf"
        # output_file = "../Test_4_pages_A.pdf"
        # creator_str = "its me"

        # error_code = self.test_obj.set_task_metadata_parameter(input_file, output_file, creator_str)
        # error_code = self.test_obj.open_pdf()
        # self.test_obj._print_metadata()
