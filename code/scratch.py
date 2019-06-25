for n in contents:
    if n.is_dir() and n.name.startswith('etdadmin'):
        cur_path = n.path
        for p in scandir(cur_path):
            if p.name.endswith('.xml'):
                xml_doc = ET.parse(p.path)
                xml_root = xml_doc.getroot()
                title = xml_root.find("DISS_description/DISS_title")
                author_surname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/"+"DISS_name/DISS_surname")
                author_fname = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_fname")
                
                author_middle = xml_root.find("DISS_authorship/DISS_author[@type='primary']/DISS_name/DISS_middle") ####
                advisor_surname = xml_root.find("DISS_advisor/DISS_author/DISS_surname") ####
                advisor_fname = xml_root.find("DISS_advisor/DISS_author/DISS_fname") ####
                advisor_middle = xml_root.find("DISS_advisor/DISS_author/DISS_middle") ####
                abstract = xml_root.find("DISS_abstract") ####
                embargo = xml_root.find("DISS_submission[@embargo_code]") ####
                pages = xml_root.find("DISS_description[@page_count]") ####
                dot = xml_root.find("DISS_description[@kind]") ####
                #aek dot= dissertation or thesis 
                dept = xml_root.find("DISS_description/DISS_institution/DISS_inst_contact") ####
               
                comp_date = xml_root.find("DISS_description/DISS_dates/DISS_comp_date")
                license = xml_root.find("DISS_creative_commons_license/DISS_abbreviation")
                acceptance = xml_root.find("DISS_repository/DISS_acceptance")
                sales_restriction = xml_root.find("DISS_restriction/DISS_sales_restriction")
                
                if title != None:
                    title_text = title.text.encode('utf-8')
                else:
                    title_text = b"null"
                if author_fname != None and author_middle != None and author_surname != None:
                    author_text = author_surname.text.encode('utf-8') + , b" " + author_fname.text.encode('utf-8') + b" " + author_middle.text.encode('utf-8')
                else:
                    author_text = b"null"        
                if inst_contact != None:
                    inst_contact_text = inst_contact.text.encode('utf-8')
                else:
                    inst_contact_text = b"null"
                if comp_date != None:
                    comp_date_text = comp_date.text.encode('utf-8')
                    
                if dot != 'Doctoral' and inst_contact != None:
                    deg_name = 'Doctor of Philosophy in'.text.encode('utf-8') + b" " + dept.text.encode('utf-8')    ####
                else:
                    deg_name = b"null"
                    
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
                    
                if dot = 'Doctoral' and inst_contact != None: ####
                    deg_name = 'Doctor of Philosophy in'.text.encode('utf-8') + b" " + dept.text.encode('utf-8')    ####
                else:
                    deg_name = b"null" ####
                
                line = [title_text, author_text, inst_contact_text, comp_date_text, license_text, acceptance_text, sales_restriction_text]
                all_lines.append(line)
                count += 1