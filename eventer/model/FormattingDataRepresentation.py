class FormattingDataRepresentation:

    @staticmethod
    def convert_from_iterator_to_string(source):
        """
        Method converts set or list or other iterator type to formatted string with '|' delimiter
        :param source:
        :return:
        """
        final_string = ""
        if len(source) == 0:
            return final_string
        for element in source:
            final_string += str(element)
            final_string += "|"
        final_string = final_string[:-1]  # Remove last symbol "|"
        return final_string
