import os


def find_html_files(directory):
    #create a variable with all files with '.html' ending
    html_files = []
    # go throught all the files in the directory and subdirectory
    for subdir, _, files in os.walk(directory):
        for file in files:
            # find all files with '.html' ending by endswitch method.
            if file.endswith('.html'):
                # in case HTML file was found add the path and file name to the html_file_path variable for further
                # check of the i18n attribute presence inside the tags
                html_file_path = os.path.join(subdir, file)
                html_files.append(html_files)
                # Open all HTML files
                with open(html_file_path, 'r', encoding='utf-8') as html:
                    str_counter = 0
                    # go throught all lines to validate the presence of i18n attribute for p, button, h2 and h tags
                    for str in html:
                        str_counter += 1
                        # Check all necessary tags for i18 attribute and if not i18 output the error
                        if '<p>' in str and 'i18n' not in html:
                            print(f" tag <p> without i18n attribute in {html_file_path}, on line: {str_counter}")
                        if '<button>' in str and 'i18n' not in html:
                            print(f" tag <button> without i18n attribute on {html_file_path}, on line: {str_counter}")
                        if '<h2>' in str and 'i18n' not in html:
                            print(f" tag <h2> without i18n attribute on {html_file_path}, on line: {str_counter}")
                        if '<h>' in str and 'i18n' not in html:
                            print(f" tag <h> without i18n attribute on {html_file_path}, on line: {str_counter}")
    return html_files


path = 'C:/Users/Andrei_Hudkou2/Desktop/Learn/Python/tms_qap-18_Gudkov/exam_python_basic/test-i18n/app'
html_files = find_html_files(path)
