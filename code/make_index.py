import csv
from os import scandir
from sys import stderr, stdout
from xml.etree import ElementTree as ET

directory = "/Users/akierig/dspace_etd/bozo/unzipped"

contents = scandir(directory)

count = 0
all_lines = []

for n in contents:
    if n.is_dir() and n.name.startswith('etdadmin'):
        cur_path = n.path
        for p in scandir(cur_path):
            if p.name.endswith('.xml'):
                xml_doc = ET.parse(p.path)
                xml_root = xml_doc.getroot()
                embargo = xml_root.find("<DISS_submission/embargo_code")
                advisorl = xml_root.find("<DISS_advisor>/DISS_name/DISS_surname")
                advisorf = xml_root.find ("<DISS_advisor>/DISS_name/DISS_fname")
                advisorm = xml_root.find ("<DISS_advisor>/DISS_name/DISS_middle")
                author_fname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_fname")
                author_middle = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_middle")
                author_surname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/"+"DISS_name/DISS_surname")
                date = xml_root.find("DISS_description/DISS_dates/DISS_comp_date")
                abstract = xml_root.find("DISS_abstract")
                extent = xml_root.find("")

                inst_contact = xml_root.find("DISS_description/DISS_institution/DISS_inst_contact")
				
                title = xml_root.find("DISS_description/DISS_title")


                license = xml_root.find("DISS_creative_commons_license/DISS_abbreviation")
                acceptance = xml_root.find("DISS_repository/DISS_acceptance")
                sales_restriction = xml_root.find("DISS_restriction/DISS_sales_restriction")
                if title != None:
                    title_text = title.text.encode('utf-8')
                else:
                    title_text = b"null"
                if author_fname != None and author_surname != None:
                    author_text = author_fname.text.encode('utf-8') + b" " + author_surname.text.encode('utf-8')
                else:
                    author_text = b"null"
                if author_fname != None and author_surname != None:
                    author_text = author_fname.text.encode('utf-8') + b" " + author_surname.text.encode('utf-8')
                else:
                    author_text = b"null"
                if inst_contact != None:
                    inst_contact_text = inst_contact.text.encode('utf-8')
                else:
                    inst_contact_text = b"null"
                if comp_date != None:
                    comp_date_text = comp_date.text.encode('utf-8')
                else:
                    comp_date_text = b"null"
                if license != None:
                    license_text = license.text.encode('utf-8')
                else:
                    license_text = b"null"
                if acceptance != None:
                    acceptance_text = str(acceptance.text).encode('utf-8')
                else:
                    acceptance_text = b"null"
                if sales_restriction != None:
                    sales_restriction_text = str(sales_restriction.get('code')).encode('utf-8')
                else:
                    sales_restriction_text = b"null"
                line = [title_text, author_text, inst_contact_text, comp_date_text, license_text, acceptance_text, sales_restriction_text]
                all_lines.append(line)
                count += 1


with open("/Users/akierig/dspace_etd/saf/dspace.csv", "w") as writingfile:
    aWriter = csv.writer(writingfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    aWriter.writerow([
                  "title", "author", "comp_date", "inst_contact", "license",
                  "acceptance_text", "sales_restriction"
# Add new variables to line above #
                 ])
    for line in all_lines:
        aWriter.writerow(line)

print(len(all_lines))
print(count)
print("There are {} total valid dissertations".format(str(count)))
