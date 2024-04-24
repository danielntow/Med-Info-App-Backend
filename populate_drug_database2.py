# populate_drug_database.py


import os
import django
from django.db import transaction

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


# @transaction.atomic
def populate_database():
    drugs = [
        {
            'name': 'Amoxicillin Clavulanic Acid',
            'dosage': ('Dosage regimen varies based on the specific indication and severity of the infection. '
                       'Typically administered orally at doses ranging from 250 mg to 875 mg of amoxicillin every 8-12 hours, '
                       'depending on the formulation and severity of the infection. The clavulanic acid component is typically '
                       'administered in a fixed ratio with amoxicillin, such as 125 mg or 250 mg.\n'
                       'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
            'indication': ('Treatment of bacterial infections such as respiratory tract infections, '
                           'urinary tract infections, and skin and soft tissue infections.'),
            'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
                        'Use caution in individuals with a history of penicillin allergy or renal impairment.'),
            'administration': ('Administered orally with or without food. '
                               'Tablets or suspension should be taken with a full glass of water.'),
            'pregnancy_lactation': ('Limited data is available regarding the safety of amoxicillin clavulanic acid during pregnancy and lactation. '
                                    'Consult healthcare provider before use.'),
            'contraindication': 'Hypersensitivity to amoxicillin, clavulanic acid, or any penicillin antibiotic.',
            'adverse_effects': ('Common side effects include diarrhea, nausea, vomiting, or rash. '
                                'Severe allergic reactions such as anaphylaxis may occur in rare cases.')
        },
        {
            'name': 'Augmentin',
            'dosage': ('Dosage regimen varies based on the specific indication and severity of the infection. '
                       'Typically administered orally at doses ranging from 250 mg to 875 mg of amoxicillin every 8-12 hours, '
                       'depending on the formulation and severity of the infection. The clavulanic acid component is typically '
                       'administered in a fixed ratio with amoxicillin, such as 125 mg or 250 mg.\n'
                       'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
            'indication': ('Treatment of bacterial infections such as respiratory tract infections, '
                           'urinary tract infections, and skin and soft tissue infections.'),
            'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
                        'Use caution in individuals with a history of penicillin allergy or renal impairment.'),
            'administration': ('Administered orally with or without food. '
                               'Tablets or suspension should be taken with a full glass of water.'),
            'pregnancy_lactation': ('Limited data is available regarding the safety of Augmentin during pregnancy and lactation. '
                                    'Consult healthcare provider before use.'),
            'contraindication': 'Hypersensitivity to amoxicillin, clavulanic acid, or any penicillin antibiotic.',
            'adverse_effects': ('Common side effects include diarrhea, nausea, vomiting, or rash. '
                                'Severe allergic reactions such as anaphylaxis may occur in rare cases.')
        },
        {
            'name': 'Methyldopa',
            'dosage': ('Initial dose: 250 mg orally 2-3 times daily. '
                       'May increase gradually based on response and tolerance, up to a maximum of 2 g per day.\n'
                       'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
            'indication': ('Treatment of hypertension, particularly during pregnancy.'),
            'warning': ('May cause orthostatic hypotension, drowsiness, or hemolytic anemia. '
                        'Use caution in individuals with a history of depression or hepatic impairment.'),
            'administration': ('Administered orally with or without food. '
                               'Tablets should be swallowed whole with a full glass of water.'),
            'pregnancy_lactation': ('Limited data is available regarding the safety of methyldopa during pregnancy and lactation. '
                                    'Consult healthcare provider before use.'),
            'contraindication': ('Hypersensitivity to methyldopa or any component of the formulation. '
                                 'Also contraindicated in patients with active liver disease or history of liver disorders.'),
            'adverse_effects': ('Common side effects include dizziness, drowsiness, headache, or gastrointestinal disturbances. '
                                'Rare side effects may include liver toxicity or hemolytic anemia.')
        },
        {
            'name': 'Clindamycin',
            'dosage': ('Dosage regimen varies based on the specific indication and severity of the infection. '
                       'Typically administered orally at doses ranging from 150 mg to 450 mg every 6-8 hours.\n'
                       'For severe infections, intravenous administration may be necessary.'),
            'indication': ('Treatment of bacterial infections such as skin and soft tissue infections, '
                           'anaerobic infections, and pelvic inflammatory disease.'),
            'warning': ('May cause gastrointestinal disturbances, allergic reactions, or pseudomembranous colitis. '
                        'Use caution in individuals with a history of colitis or hepatic impairment.'),
            'administration': ('Administered orally with or without food. '
                               'Tablets or capsules should be swallowed whole with a full glass of water.'),
            'pregnancy_lactation': ('Limited data is available regarding the safety of clindamycin during pregnancy and lactation. '
                                    'Consult healthcare provider before use.'),
            'contraindication': 'Hypersensitivity to clindamycin or any lincomycin antibiotic.',
            'adverse_effects': ('Common side effects include diarrhea, nausea, vomiting, or rash. '
                                'Severe allergic reactions may occur in rare cases, along with pseudomembranous colitis.')
        },
        {
            'name': 'Phlebodia',
            'dosage': ('Recommended dose is typically 600 mg orally once daily, preferably in the morning before meals.'),
            'indication': ('Treatment of chronic venous insufficiency and related symptoms such as leg swelling, pain, and heaviness.'),
            'warning': ('May cause gastrointestinal disturbances or headache. '
                        'Use caution in individuals with a history of cardiovascular disorders or liver impairment.'),
            'administration': ('Administered orally, preferably in the morning before meals. '
                               'Tablets should be swallowed whole with a full glass of water.'),
            'pregnancy_lactation': ('Limited data is available regarding the safety of Phlebodia during pregnancy and lactation. '
                                    'Consult healthcare provider before use.'),
            'contraindication': ('Hypersensitivity to diosmin or any component of the formulation. '
                                 'Also contraindicated in patients with severe liver disease or history of thromboembolic disorders.'),
            'adverse_effects': ('Common side effects include gastrointestinal disturbances or headache. '
                                'Rare side effects may include allergic reactions or dizziness.')
        }
    ]

    # drugs = [
    # {
    #     'name': 'Malarone',
    #     'dosage': ('Adults: 1 tablet daily with food, starting 1-2 days before travel to the malaria-endemic area '
    #                'and continuing throughout the stay and for 7 days after leaving the area.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Prophylaxis of Plasmodium falciparum malaria in individuals traveling to endemic areas.'),
    #     'warning': ('Should be used with caution in individuals with a history of psychiatric disorders or seizures. '
    #                 'Discontinue use if psychiatric or neurological symptoms occur.'),
    #     'administration': ('Administered orally with food. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of Malarone during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to atovaquone, proguanil, or any component of the formulation.',
    #     'adverse_effects': 'Common adverse effects include nausea, vomiting, headache, and abdominal pain.'
    # },
    # {
    #     'name': 'Proguanil',
    #     'dosage': ('Adults: 200 mg (2 tablets) daily, starting 1-2 days before travel to the malaria-endemic area '
    #                'and continuing throughout the stay and for 7 days after leaving the area.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Prophylaxis of Plasmodium falciparum malaria in individuals traveling to endemic areas. '
    #                    'Used in combination with other antimalarial agents such as atovaquone.'),
    #     'warning': ('Should be used with caution in individuals with a history of hepatic impairment or renal impairment. '
    #                 'Discontinue use if gastrointestinal disturbances or rash occur.'),
    #     'administration': ('Administered orally with food. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of proguanil during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to proguanil or any component of the formulation.',
    #     'adverse_effects': 'Common adverse effects include gastrointestinal disturbances and headache.'

    # },
    # {
    #     'name': 'Doxycycline',
    #     'dosage': ('Adults: 100 mg orally once daily, starting 1-2 days before travel to the malaria-endemic area '
    #                'and continuing throughout the stay and for 28 days after leaving the area.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Prophylaxis of Plasmodium falciparum malaria in individuals traveling to endemic areas. '
    #                    'Also indicated for the treatment of various bacterial infections.'),
    #     'warning': ('May cause gastrointestinal disturbances, photosensitivity reactions, or vaginal candidiasis. '
    #                 'Use caution in individuals with a history of liver disease or renal impairment.'),
    #     'administration': ('Administered orally with food. '
    #                        'Capsules or tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Should not be used during pregnancy due to the risk of tooth discoloration and '
    #                             'skeletal development abnormalities in the fetus. Avoid use during lactation.'),
    #     'contraindication': 'Hypersensitivity to doxycycline or any tetracycline antibiotic.',
    #     'adverse_effects': 'Common adverse effects include nausea, vomiting, and diarrhea.'
    # },
    # {
    #     'name': 'Secnidazole',
    #     'dosage': ('Recommended dose for adults is typically 2 g as a single dose.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Treatment of bacterial and protozoal infections such as giardiasis, trichomoniasis, '
    #                    'and bacterial vaginosis.'),
    #     'warning': ('May cause gastrointestinal disturbances, headache, or dizziness. '
    #                 'Use caution in individuals with a history of neurological disorders or hepatic impairment.'),
    #     'administration': ('Administered orally, preferably with or after meals. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of secnidazole during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to secnidazole or any nitroimidazole derivative.',
    #     'adverse_effects': 'Common adverse effects include nausea, vomiting, and metallic taste.'
    # },
    # {
    #     'name': 'Cefuroxime',
    #     'dosage': ('Dosage regimen varies based on the specific indication and severity of the infection. '
    #                'Typically administered orally or intravenously at doses ranging from 250 mg to 1.5 g every 8-12 hours.'),
    #     'indication': ('Treatment of bacterial infections such as community-acquired pneumonia, urinary tract infections, '
    #                    'and skin and soft tissue infections.'),
    #     'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
    #                 'Use caution in individuals with a history of penicillin allergy or renal impairment.'),
    #     'administration': ('Administered orally with or without food. '
    #                        'Intravenous administration is indicated for severe infections or when oral therapy is not feasible.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of cefuroxime during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to cefuroxime or any cephalosporin antibiotic.',
    #     'adverse_effects': 'Common adverse effects include diarrhea, nausea, and rash.'
    # },
    # {
    #     'name': 'Cefixime',
    #     'dosage': ('Recommended dose for adults is typically 400 mg orally once daily or divided into two doses.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Treatment of bacterial infections such as respiratory tract infections, urinary tract infections, '
    #                    'and gonorrhea.'),
    #     'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
    #                 'Use caution in individuals with a history of penicillin allergy or renal impairment.'),
    #     'administration': ('Administered orally, preferably with or after meals. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of cefixime during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to cefixime or any cephalosporin antibiotic.',
    #     'adverse_effects': 'Common adverse effects include diarrhea, nausea, and abdominal pain.'
    # },
    # {
    #     'name': 'Ceftriaxone',
    #     'dosage': ('Dosage regimen varies based on the specific indication and severity of the infection. '
    #                'Typically administered intravenously or intramuscularly at doses ranging from 1 g to 2 g once daily.'),
    #     'indication': ('Treatment of bacterial infections such as meningitis, gonorrhea, and intra-abdominal infections.'),
    #     'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
    #                 'Use caution in individuals with a history of cephalosporin allergy or renal impairment.'),
    #     'administration': ('Administered intravenously or intramuscularly. '
    #                        'Reconstitution and dilution instructions should be followed carefully.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of ceftriaxone during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to ceftriaxone or any cephalosporin antibiotic.',
    #     'adverse_effects': 'Common adverse effects include diarrhea, nausea, and injection site reactions.'
    # },
    # {
    #     'name': 'Norfloxacin',
    #     'dosage': ('Recommended dose for adults is typically 400 mg orally twice daily.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Treatment of urinary tract infections, gonorrhea, and prostatitis caused by susceptible bacteria.'),
    #     'warning': ('May cause gastrointestinal disturbances, dizziness, or photosensitivity reactions. '
    #                 'Use caution in individuals with a history of neurological disorders or renal impairment.'),
    #     'administration': ('Administered orally, preferably with a full glass of water. '
    #                        'Tablets should not be chewed or crushed.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of norfloxacin during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to norfloxacin or any fluoroquinolone antibiotic.',

    #     'adverse_effects': 'Common adverse effects include nausea, headache, and dizziness.'
    # },
    # {
    #     'name': 'Clotrimazole',
    #     'dosage': ('Dosage regimen varies based on the specific indication and severity of the fungal infection. '
    #                'Typically applied topically as a cream, lotion, or solution to the affected area.'),
    #     'indication': ('Treatment of fungal infections such as athlete\'s foot, jock itch, ringworm, '
    #                    'and vaginal yeast infections.'),
    #     'warning': ('May cause local irritation, burning, or itching at the application site. '
    #                 'Use caution in individuals with a history of hypersensitivity reactions to imidazoles '
    #                 'or other antifungal agents.'),
    #     'administration': ('Administered topically to the affected area. '
    #                        'Creams or lotions should be applied thinly and evenly.'),
    #     'pregnancy_lactation': ('Limited data is available regarding the safety of clotrimazole during pregnancy and lactation. '
    #                             'Consult healthcare provider before use.'),
    #     'contraindication': 'Hypersensitivity to clotrimazole or any azole antifungal.',
    #     'adverse_effects': 'Common adverse effects include local irritation and itching.'

    # },
    # {
    #     'name': 'Fluconazole',
    #     'dosage': ('Dosage regimen varies based on the specific indication and severity of the fungal infection. '
    #                'Typically administered orally at doses ranging from 50 mg to 400 mg once daily.'),
    #     'indication': ('Treatment of fungal infections such as candidiasis, cryptococcal meningitis, '
    #                    'and various systemic fungal infections.'),
    #     'warning': ('May cause gastrointestinal disturbances, headache, or rash. '
    #                 'Use caution in individuals with a history of liver disease or renal impairment.'),
    #     'administration': ('Administered orally with or without food. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Should be used with caution during pregnancy, especially during the first trimester. '
    #                             'Limited data is available regarding the safety of fluconazole during lactation.'),
    #     'contraindication': 'Hypersensitivity to fluconazole or any azole antifungal.',
    #     'adverse_effects': 'Common adverse effects include nausea, headache, and abdominal pain.'

    # },
    # {
    #     'name': 'Amitriptyline',
    #     'dosage': ('Initial dose: 25 mg orally once daily at bedtime. '
    #                'May increase gradually based on response and tolerance, up to a maximum of 150 mg per day.\n'
    #                'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #     'indication': ('Treatment of depression, neuropathic pain, migraine prophylaxis, '
    #                    'and insomnia.'),
    #     'warning': ('May cause sedation, anticholinergic effects, or orthostatic hypotension. '
    #                 'Use caution in individuals with a history of cardiac conduction abnormalities or seizures.'),
    #     'administration': ('Administered orally with or without food. '
    #                        'Tablets should be swallowed whole with a full glass of water.'),
    #     'pregnancy_lactation': ('Should be used with caution during pregnancy, especially during the first trimester. '
    #                             'Limited data is available regarding the safety of amitriptyline during lactation.'),
    #     'contraindication': 'Hypersensitivity to amitriptyline or any tricyclic antidepressant.',
    #     'adverse_effects': 'Common adverse effects include sedation, dry mouth, and dizziness.'
    # },
    #     {
    #         'name': 'Hydroxyzine',
    #         'dosage': ('Adults: 25-100 mg orally 3-4 times daily as needed for anxiety or pruritus.\n'
    #                    'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #         'indication': ('Treatment of anxiety, pruritus, and allergic conditions such as urticaria and atopic dermatitis.'),
    #         'warning': ('May cause sedation, anticholinergic effects, or QT prolongation. '
    #                     'Use caution in individuals with a history of cardiac arrhythmias or glaucoma.'),
    #         'administration': ('Administered orally with or without food. '
    #                            'Tablets should be swallowed whole with a full glass of water.'),
    #         'pregnancy_lactation': ('Limited data is available regarding the safety of hydroxyzine during pregnancy and lactation. '
    #                                 'Consult healthcare provider before use.'),
    #         'contraindication': 'Hypersensitivity to hydroxyzine or any piperazine derivative.',
    #         'adverse_effects': 'Common adverse effects include sedation, dry mouth, and dizziness.'
    #     },
    #     {
    #         'name': 'Ranitidine',
    #         'dosage': ('Adults: 150 mg orally twice daily or 300 mg orally once daily, preferably at bedtime.\n'
    #                    'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #         'indication': ('Treatment of gastroesophageal reflux disease (GERD), peptic ulcer disease, '
    #                        'and dyspepsia.'),
    #         'warning': ('May cause headache, gastrointestinal disturbances, or elevated liver enzymes. '
    #                     'Use caution in individuals with a history of renal impairment or porphyria.'),
    #         'administration': ('Administered orally with or without food. '
    #                            'Tablets should be swallowed whole with a full glass of water.'),
    #         'pregnancy_lactation': ('Limited data is available regarding the safety of ranitidine during pregnancy and lactation. '
    #                                 'Consult healthcare provider before use.'),
    #         'contraindication': 'Hypersensitivity to ranitidine or any histamine H2-receptor antagonist.',

    #         'adverse_effects': 'Common adverse effects include headache, nausea, and abdominal pain.'
    #     },
    #     {
    #         'name': 'Metronidazole',
    #         'dosage': ('Adults: 500 mg orally twice daily for 7-10 days, depending on the specific infection being treated.\n'
    #                    'Pediatric dose is weight-based: consult healthcare provider for appropriate dosing.'),
    #         'indication': ('Treatment of bacterial and protozoal infections such as giardiasis, trichomoniasis, '
    #                        'and bacterial vaginosis.'),
    #         'warning': ('May cause gastrointestinal disturbances, headache, or metallic taste. '
    #                     'Use caution in individuals with a history of neurologic disorders or hepatic impairment.'),
    #         'administration': ('Administered orally with or without food. '
    #                            'Tablets should be swallowed whole with a full glass of water.'),
    #         'pregnancy_lactation': ('Should be used with caution during pregnancy, especially during the first trimester. '
    #                                 'Avoid use during lactation.'),
    #         'contraindication': 'Hypersensitivity to metronidazole or any nitroimidazole derivative.',
    #         'adverse_effects': 'Common adverse effects include nausea, headache, and metallic taste.'
    #     },
    #     {
    #         'name': 'Cefepime',
    #         'dosage': ('Dosage regimen varies based on the specific indication, severity of the infection, and renal function. '
    #                    'Typically administered intravenously at doses ranging from 1 g to 2 g every 8-12 hours.'),
    #         'indication': ('Treatment of severe bacterial infections such as pneumonia, septicemia, '
    #                        'and intra-abdominal infections.'),
    #         'warning': ('May cause gastrointestinal disturbances, allergic reactions, or superinfections. '
    #                     'Use caution in individuals with a history of cephalosporin allergy or renal impairment.'),
    #         'administration': ('Administered intravenously over 30 minutes to 2 hours. '
    #                            'Reconstitution and dilution instructions should be followed carefully.'),
    #         'pregnancy_lactation': ('Limited data is available regarding the safety of cefepime during pregnancy and lactation. '
    #                                 'Consult healthcare provider before use.'),
    #         'contraindication': 'Hypersensitivity to cefepime or any cephalosporin antibiotic.',
    #         'adverse_effects': 'Common adverse effects include diarrhea, nausea, and headache.'
    #     }
    # ]

    # drugs = [
    #     {
    #         'name': 'Acyclovir',
    #         'dosage': 'Dosage regimen varies based on the specific indication and severity of the infection. Typically administered orally, intravenously, or topically at doses ranging from 200 mg to 800 mg orally 5 times daily for 5-10 days.',
    #         'indication': 'Treatment of herpes simplex virus infections, varicella-zoster virus infections, and herpes zoster infections.',
    #         'warning': 'May cause gastrointestinal disturbances, headache, or renal impairment. Use caution in individuals with a history of renal disease or neurologic disorders.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of acyclovir during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include nausea, vomiting, and diarrhea.',
    #         'contraindication': 'Contraindicated in individuals with hypersensitivity to acyclovir or valacyclovir.'
    #     },
    #     {
    #         'name': 'Diphenhydramine',
    #         'dosage': 'Adults: 25-50 mg orally 3-4 times daily as needed for allergy or pruritus.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of allergic conditions such as allergic rhinitis, urticaria, and atopic dermatitis. Also used as a sedative and antipruritic agent.',
    #         'warning': 'May cause sedation, anticholinergic effects, or paradoxical excitability. Use caution in individuals with a history of narrow-angle glaucoma or urinary retention.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of diphenhydramine during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include drowsiness, dry mouth, and blurred vision.',
    #         'contraindication': 'Contraindicated in individuals with hypersensitivity to diphenhydramine or other antihistamines.'
    #     },
    #     {
    #         'name': 'Ondansetron',
    #         'dosage': 'Adults: 8 mg orally 3 times daily as needed for nausea and vomiting.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Prevention and treatment of nausea and vomiting associated with chemotherapy, radiation therapy, and surgery.',
    #         'warning': 'May cause headache, constipation, or QT prolongation. Use caution in individuals with a history of cardiac arrhythmias or serotonin syndrome.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of ondansetron during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, constipation, and dizziness.',
    #         'contraindication': 'Contraindicated in individuals with hypersensitivity to ondansetron or other selective 5-HT3 receptor antagonists.'
    #     },
    #     {
    #         'name': 'Furosemide',
    #         'dosage': 'Adults: 20-80 mg orally once daily or 40-120 mg intravenously once daily, depending on the specific indication and renal function.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of edema associated with congestive heart failure, cirrhosis, or renal disease. Also used for the management of hypertension.',
    #         'warning': 'May cause electrolyte imbalances, hypotension, or ototoxicity. Use caution in individuals with a history of sulfonamide allergy or gout.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of furosemide during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include hypokalemia, dehydration, and hypotension.',
    #         'contraindication': 'Contraindicated in individuals with anuria, hypersensitivity to sulfonamides, or electrolyte depletion.'
    #     },
    #     {
    #         'name': 'Hydrocortisone',
    #         'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and route of administration. Typically administered topically, orally, or intravenously at doses ranging from 5 mg to 100 mg daily.',
    #         'indication': 'Treatment of inflammatory and allergic conditions such as dermatitis, asthma, and rheumatoid arthritis. Also used for adrenal insufficiency and shock.',
    #         'warning': 'May cause adrenal suppression, immunosuppression, or glucose intolerance. Use caution in individuals with a history of peptic ulcer disease or systemic fungal infections.',
    #         'administration': 'Administered orally, topically, or intravenously. Follow specific dosing instructions provided by healthcare provider.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of hydrocortisone during lactation.',
    #         'adverse_effects': 'Common adverse effects include adrenal suppression, insomnia, and fluid retention.',
    #         'contraindication': 'Contraindicated in individuals with systemic fungal infections or known hypersensitivity to hydrocortisone or other corticosteroids.'
    #     },
    #     {
    #         'name': 'Folic acid',
    #         'dosage': 'Dosage regimen varies based on the specific indication and patient characteristics. Typically administered orally at doses ranging from 0.4 mg to 5 mg daily.',
    #         'indication': 'Prevention and treatment of folate deficiency, megaloblastic anemia, and neural tube defects in pregnancy.',
    #         'warning': 'May mask symptoms of pernicious anemia or vitamin B12 deficiency. Use caution in individuals with a history of seizures or psychiatric disorders.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Supplementation with folic acid is recommended during pregnancy to prevent neural tube defects. Consult healthcare provider for appropriate dosing.',
    #         'adverse_effects': 'Common adverse effects include nausea, abdominal bloating, and flatulence.',
    #         'contraindication': 'Contraindicated in individuals with untreated vitamin B12 deficiency or hypersensitivity to folic acid.'
    #     },
    #     {
    #         'name': 'Metoclopramide',
    #         'dosage': 'Adults: 10-15 mg orally or intravenously 3-4 times daily, 30 minutes before meals and at bedtime.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of gastroesophageal reflux disease (GERD), diabetic gastroparesis, and chemotherapy-induced nausea and vomiting.',
    #         'warning': 'May cause extrapyramidal symptoms, tardive dyskinesia, or neuroleptic malignant syndrome. Use caution in individuals with a history of gastrointestinal bleeding or Parkinson\'s disease.',
    #         'administration': 'Administered orally or intravenously. Oral tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of metoclopramide during lactation.',
    #         'adverse_effects': 'Common adverse effects include drowsiness, restlessness, and diarrhea.',
    #         'contraindication': 'Contraindicated in individuals with pheochromocytoma, history of tardive dyskinesia, or gastrointestinal obstruction.'
    #     },
    #     {
    #         'name': 'Hydrochlorothiazide',
    #         'dosage': 'Initial dose: 12.5-25 mg orally once daily, titrated based on response.\nMaximum dose: 50 mg orally once daily.',
    #         'indication': 'Treatment of hypertension, edema associated with congestive heart failure, and nephrotic syndrome.',
    #         'warning': 'May cause electrolyte imbalances, hypotension, or hyperglycemia. Use caution in individuals with a history of sulfonamide allergy or renal impairment.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of hydrochlorothiazide during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include hypokalemia, dizziness, and photosensitivity.',
    #         'contraindication': 'Contraindicated in individuals with anuria, hypersensitivity to sulfonamides, or severe renal impairment.'
    #     },
    #     {
    #         'name': 'Carvedilol',
    #         'dosage': 'Initial dose: 3.125 mg orally twice daily, titrated based on response.\nMaintenance dose: 6.25-25 mg orally twice daily.\nMaximum dose: 50 mg orally twice daily.',
    #         'indication': 'Treatment of heart failure, hypertension, and left ventricular dysfunction following myocardial infarction.',
    #         'warning': 'May cause bradycardia, hypotension, or heart block. Use caution in individuals with a history of asthma or chronic obstructive pulmonary disease.',
    #         'administration': 'Administered orally with food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of carvedilol during lactation.',
    #         'adverse_effects': 'Common adverse effects include hypotension, dizziness, and fatigue.',
    #         'contraindication': 'Contraindicated in individuals with decompensated heart failure, bronchial asthma, or severe bradycardia.'
    #     },
    #     {
    #         'name': 'Nitroglycerin',
    #         'dosage': 'Sublingual tablets: 0.3-0.6 mg sublingually every 5 minutes as needed for angina.\nOral capsules or tablets: 2.5-9 mg orally 3-4 times daily, with the last dose given before bedtime for prophylaxis of angina.\nTransdermal patch: 0.2-0.4 mg/hr applied topically once daily, with patch-free interval to prevent tolerance.',
    #         'indication': 'Treatment and prophylaxis of angina pectoris, acute myocardial infarction, and heart failure.',
    #         'warning': 'May cause headache, hypotension, or reflex tachycardia. Use caution in individuals with a history of intracranial hemorrhage or severe anemia.',
    #         'administration': 'Sublingual tablets should be placed under the tongue and allowed to dissolve. Oral capsules or tablets should be swallowed whole with a full glass of water. Transdermal patches should be applied to clean, dry skin and rotated to different sites.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of nitroglycerin during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, dizziness, and hypotension.',
    #         'contraindication': 'Contraindicated in individuals with severe anemia, hypotension, or concomitant use of phosphodiesterase inhibitors.'
    #     }
    # ]

    # drugs = [
    #     {
    #         'name': 'Acyclovir',
    #         'dosage': 'Dosage regimen varies based on the specific indication and severity of the infection. Typically administered orally, intravenously, or topically at doses ranging from 200 mg to 800 mg orally 5 times daily for 5-10 days.',
    #         'indication': 'Treatment of herpes simplex virus infections, varicella-zoster virus infections, and herpes zoster infections.',
    #         'warning': 'May cause gastrointestinal disturbances, headache, or renal impairment. Use caution in individuals with a history of renal disease or neurologic disorders.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of acyclovir during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include gastrointestinal disturbances, headache, and renal impairment.'
    #     },
    #     {
    #         'name': 'Diphenhydramine',
    #         'dosage': 'Adults: 25-50 mg orally 3-4 times daily as needed for allergy or pruritus.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of allergic conditions such as allergic rhinitis, urticaria, and atopic dermatitis. Also used as a sedative and antipruritic agent.',
    #         'warning': 'May cause sedation, anticholinergic effects, or paradoxical excitability. Use caution in individuals with a history of narrow-angle glaucoma or urinary retention.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of diphenhydramine during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include sedation, dizziness, and ataxia.'
    #     },
    #     {
    #         'name': 'Ondansetron',
    #         'dosage': 'Adults: 8 mg orally 3 times daily as needed for nausea and vomiting.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Prevention and treatment of nausea and vomiting associated with chemotherapy, radiation therapy, and surgery.',
    #         'warning': 'May cause headache, constipation, or QT prolongation. Use caution in individuals with a history of cardiac arrhythmias or serotonin syndrome.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of ondansetron during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, constipation, and QT prolongation.'
    #     },
    #     {
    #         'name': 'Furosemide',
    #         'dosage': 'Adults: 20-80 mg orally once daily or 40-120 mg intravenously once daily, depending on the specific indication and renal function.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of edema associated with congestive heart failure, cirrhosis, or renal disease. Also used for the management of hypertension.',
    #         'warning': 'May cause electrolyte imbalances, hypotension, or ototoxicity. Use caution in individuals with a history of sulfonamide allergy or gout.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of furosemide during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include electrolyte imbalances, hypotension, and ototoxicity.'
    #     },
    #     {
    #         'name': 'Hydrocortisone',
    #         'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and route of administration. Typically administered topically, orally, or intravenously at doses ranging from 5 mg to 100 mg daily.',
    #         'indication': 'Treatment of inflammatory and allergic conditions such as dermatitis, asthma, and rheumatoid arthritis. Also used for adrenal insufficiency and shock.',
    #         'warning': 'May cause adrenal suppression, immunosuppression, or glucose intolerance. Use caution in individuals with a history of peptic ulcer disease or systemic fungal infections.',
    #         'administration': 'Administered orally, topically, or intravenously. Follow specific dosing instructions provided by healthcare provider.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of hydrocortisone during lactation.',
    #         'adverse_effects': 'Common adverse effects include adrenal suppression, immunosuppression, and glucose intolerance.'
    #     },
    #     {
    #         'name': 'Folic acid',
    #         'dosage': 'Dosage regimen varies based on the specific indication and patient characteristics. Typically administered orally at doses ranging from 0.4 mg to 5 mg daily.',
    #         'indication': 'Prevention and treatment of folate deficiency, megaloblastic anemia, and neural tube defects in pregnancy.',
    #         'warning': 'May mask symptoms of pernicious anemia or vitamin B12 deficiency. Use caution in individuals with a history of seizures or psychiatric disorders.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Supplementation with folic acid is recommended during pregnancy to prevent neural tube defects. Consult healthcare provider for appropriate dosing.',
    #         'adverse_effects': 'No common adverse effects reported.'
    #     },
    #     {
    #         'name': 'Metoclopramide',
    #         'dosage': 'Adults: 10-15 mg orally or intravenously 3-4 times daily, 30 minutes before meals and at bedtime.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of gastroesophageal reflux disease (GERD), diabetic gastroparesis, and chemotherapy-induced nausea and vomiting.',
    #         'warning': 'May cause extrapyramidal symptoms, tardive dyskinesia, or neuroleptic malignant syndrome. Use caution in individuals with a history of gastrointestinal bleeding or Parkinson\'s disease.',
    #         'administration': 'Administered orally or intravenously. Oral tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of metoclopramide during lactation.',
    #         'adverse_effects': 'Common adverse effects include extrapyramidal symptoms, sedation, and diarrhea.'
    #     },
    #     {
    #         'name': 'Hydrochlorothiazide',
    #         'dosage': 'Initial dose: 12.5-25 mg orally once daily, titrated based on response.\nMaximum dose: 50 mg orally once daily.',
    #         'indication': 'Treatment of hypertension, edema associated with congestive heart failure, and nephrotic syndrome.',
    #         'warning': 'May cause electrolyte imbalances, hypotension, or hyperglycemia. Use caution in individuals with a history of sulfonamide allergy or renal impairment.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of hydrochlorothiazide during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include electrolyte imbalances, hypotension, and dizziness.'
    #     },
    #     {
    #         'name': 'Carvedilol',
    #         'dosage': 'Initial dose: 3.125 mg orally twice daily, titrated based on response.\nMaintenance dose: 6.25-25 mg orally twice daily.\nMaximum dose: 50 mg orally twice daily.',
    #         'indication': 'Treatment of heart failure, hypertension, and left ventricular dysfunction following myocardial infarction.',
    #         'warning': 'May cause bradycardia, hypotension, or heart block. Use caution in individuals with a history of asthma or chronic obstructive pulmonary disease.',
    #         'administration': 'Administered orally with food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of carvedilol during lactation.',
    #         'adverse_effects': 'Common adverse effects include hypotension, dizziness, and fatigue.'
    #     },
    #     {
    #         'name': 'Nitroglycerin',
    #         'dosage': 'Sublingual tablets: 0.3-0.6 mg sublingually every 5 minutes as needed for angina.\nOral capsules or tablets: 2.5-9 mg orally 3-4 times daily, with the last dose given before bedtime for prophylaxis of angina.\nTransdermal patch: 0.2-0.4 mg/hr applied topically once daily, with patch-free interval to prevent tolerance.',
    #         'indication': 'Treatment and prophylaxis of angina pectoris, acute myocardial infarction, and heart failure.',
    #         'warning': 'May cause headache, hypotension, or reflex tachycardia. Use caution in individuals with a history of intracranial hemorrhage or severe anemia.',
    #         'administration': 'Sublingual tablets should be placed under the tongue and allowed to dissolve. Oral capsules or tablets should be swallowed whole with a full glass of water. Transdermal patches should be applied to clean, dry skin and rotated to different sites.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of nitroglycerin during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, hypotension, and dizziness.'
    #     },
    #     {
    #         'name': 'Spironolactone',
    #         'dosage': 'Initial dose: 25 mg orally once daily, titrated based on response.\nMaintenance dose: 25-200 mg orally once daily.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of heart failure, hypertension, and edema associated with cirrhosis or nephrotic syndrome.',
    #         'warning': 'May cause hyperkalemia, gynecomastia, or menstrual irregularities. Use caution in individuals with a history of renal impairment or hyperkalemia.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of spironolactone during lactation.',
    #         'adverse_effects': 'Common adverse effects include hyperkalemia, gynecomastia, and menstrual irregularities.'
    #     },
    #     {
    #         'name': 'Doxazosin',
    #         'dosage': 'Initial dose: 1 mg orally once daily, titrated based on response.\nMaintenance dose: 1-16 mg orally once daily, usually administered at bedtime.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Treatment of hypertension, benign prostatic hyperplasia, and urinary retention.',
    #         'warning': 'May cause orthostatic hypotension, dizziness, or syncope. Use caution in individuals with a history of hypotension or hepatic impairment.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of doxazosin during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include orthostatic hypotension, dizziness, and headache.'
    #     },
    #     {
    #         'name': 'Rabeprazole',
    #         'dosage': '20 mg orally once daily for 4-8 weeks, as part of triple therapy for Helicobacter pylori eradication.\n20 mg orally once daily for up to 8 weeks for treatment of gastroesophageal reflux disease (GERD).\nMaintenance dose: 20 mg orally once daily for long-term management of GERD.',
    #         'indication': 'Treatment of gastroesophageal reflux disease (GERD), duodenal ulcers, and Helicobacter pylori eradication.',
    #         'warning': 'May cause headache, gastrointestinal disturbances, or elevated liver enzymes. Use caution in individuals with a history of renal impairment or hepatic disease.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of rabeprazole during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, gastrointestinal disturbances, and abdominal pain.'
    #     },
    #     {
    #         'name': 'Methylprednisolone',
    #         'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and route of administration. Typically administered orally, intravenously, or topically at doses ranging from 4 mg to 1000 mg daily.',
    #         'indication': 'Treatment of inflammatory and allergic conditions such as asthma, rheumatoid arthritis, and dermatitis. Also used for adrenal insufficiency and autoimmune disorders.',
    #         'warning': 'May cause adrenal suppression, immunosuppression, or glucose intolerance. Use caution in individuals with a history of peptic ulcer disease or systemic fungal infections.',
    #         'administration': 'Administered orally, intravenously, or topically. Follow specific dosing instructions provided by healthcare provider.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of methylprednisolone during lactation.',
    #         'adverse_effects': 'Common adverse effects include adrenal suppression, immunosuppression, and increased susceptibility to infections.'
    #     },
    #     {
    #         'name': 'Esomeprazole',
    #         'dosage': '20-40 mg orally once daily for 4-8 weeks, as part of triple therapy for Helicobacter pylori eradication.\n20-40 mg orally once daily for up to 8 weeks for treatment of gastroesophageal reflux disease (GERD).\nMaintenance dose: 20 mg orally once daily for long-term management of GERD.',
    #         'indication': 'Treatment of gastroesophageal reflux disease (GERD), duodenal ulcers, and Helicobacter pylori eradication.',
    #         'warning': 'May cause headache, gastrointestinal disturbances, or elevated liver enzymes. Use caution in individuals with a history of renal impairment or hepatic disease.',
    #         'administration': 'Administered orally with or without food. Capsules should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of esomeprazole during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, gastrointestinal disturbances, and nausea.'
    #     },
    #     {
    #         'name': 'Fluticasone',
    #         'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and route of administration. Typically administered intranasally, orally, or by inhalation at doses ranging from 50 mcg to 1000 mcg daily.',
    #         'indication': 'Treatment of allergic rhinitis, asthma, and chronic obstructive pulmonary disease (COPD). Also used for nasal polyps and dermatitis.',
    #         'warning': 'May cause adrenal suppression, immunosuppression, or oral candidiasis. Use caution in individuals with a history of tuberculosis or fungal infections.',
    #         'administration': 'Administered intranasally, orally, or by inhalation. Follow specific dosing instructions provided by healthcare provider.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of fluticasone during lactation.',
    #         'adverse_effects': 'Common adverse effects include nasal dryness, throat irritation, and cough.'
    #     },
    #     {
    #         'name': 'Isosorbide mononitrate',
    #         'dosage': 'Initial dose: 20 mg orally twice daily, titrated based on response and tolerance.\nMaintenance dose: 20-120 mg orally once daily, usually administered in the morning.\nPediatric dose is weight-based: consult healthcare provider for appropriate dosing.',
    #         'indication': 'Prophylaxis of angina pectoris and treatment of heart failure.',
    #         'warning': 'May cause headache, hypotension, or reflex tachycardia. Use caution in individuals with a history of intracranial hemorrhage or severe anemia.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of isosorbide mononitrate during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include headache, hypotension, and dizziness.'
    #     },
    #     {
    #         'name': 'Warfarin',
    #         'dosage': 'Dosage regimen varies based on the specific indication, patient characteristics, and response to therapy. Typically administered orally at doses ranging from 2 mg to 10 mg once daily.',
    #         'indication': 'Prophylaxis and treatment of thromboembolic disorders such as atrial fibrillation, deep vein thrombosis, and pulmonary embolism.',
    #         'warning': 'May cause bleeding, skin necrosis, or drug interactions. Use caution in individuals with a history of hemorrhagic stroke or vitamin K deficiency.',
    #         'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #         'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the first trimester, due to teratogenic effects. Limited data is available regarding the safety of warfarin during lactation.',
    #         'adverse_effects': 'Common adverse effects include bleeding, bruising, and skin necrosis.'
    #     },
    #     {
    #         'name': 'Latanoprost',
    #         'dosage': '1 drop in the affected eye(s) once daily in the evening.',
    #         'indication': 'Treatment of open-angle glaucoma and ocular hypertension.',
    #         'warning': 'May cause ocular hyperemia, iris pigmentation, or eyelash growth. Use caution in individuals with a history of intraocular inflammation or retinal detachment.',
    #         'administration': 'Administered topically to the affected eye(s) once daily in the evening. Contact lenses should be removed before instillation and reinserted after 15 minutes.',
    #         'pregnancy_lactation': 'Limited data is available regarding the safety of latanoprost during pregnancy and lactation. Consult healthcare provider before use.',
    #         'adverse_effects': 'Common adverse effects include ocular hyperemia, blurred vision, and eye irritation.'
    #     },
    #     {
    #         'name': 'Cyclophosphamide',
    #         'dosage': 'Dosage regimen varies based on the specific indication, patient characteristics, and response to therapy. Typically administered orally, intravenously, or by injection at doses ranging from 1 mg/kg to 5 mg/kg daily.',
    #         'indication': 'Treatment of various cancers such as lymphoma, leukemia, and breast cancer. Also used for immunosuppression in autoimmune disorders.',
    #         'warning': 'May cause bone marrow suppression, hemorrhagic cystitis, or secondary malignancies. Use caution in individuals with a history of urinary tract disorders or previous exposure to alkylating agents.',
    #         'administration': 'Administered orally, intravenously, or by injection. Follow specific dosing instructions provided by healthcare provider.',
    #         'pregnancy_lactation': 'Should be avoided during pregnancy due to teratogenic effects. Limited data is available regarding the safety of cyclophosphamide during lactation.',
    #         'adverse_effects': 'Common adverse effects include bone marrow suppression, nausea, and vomiting.'
    #     }
    #     # {
    #     #     'name': 'Morphine',
    #     #     'dosage': 'Dosage varies depending on the formulation and the severity of pain. Typically administered orally, intravenously, or via other routes such as transdermal patches or epidural injections.',
    #     #     'adverse_effects': 'Common side effects include constipation, nausea, and respiratory depression. May also cause sedation, confusion, or hypotension, particularly at higher doses.',
    #     #     'indication': 'Used for the management of moderate to severe pain, particularly in cases where other analgesics are inadequate.',
    #     #     'warning': 'Requires close monitoring of respiratory function and vital signs, particularly during initiation of therapy or dosage adjustments. Should be used with caution in individuals with respiratory conditions or compromised pulmonary function.',
    #     #     'administration': 'Administered via various routes, including oral, intravenous, subcutaneous, intramuscular, and transdermal. Each route has specific dosing considerations and may require different formulations.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the third trimester, as it may cause neonatal withdrawal syndrome. Limited data is available regarding the use of morphine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to morphine or other opioids, severe respiratory depression, paralytic ileus, or acute or severe bronchial asthma.'
    #     # },
    #     # {
    #     #     'name': 'Rivaroxaban',
    #     #     'dosage': 'Typically started at 10-20 mg once daily, with or without food, for the prevention of venous thromboembolism (VTE) or stroke in individuals with atrial fibrillation.',
    #     #     'adverse_effects': 'Common side effects include bleeding, particularly gastrointestinal or intracranial bleeding. May also cause bruising, itching, or muscle pain.',
    #     #     'indication': 'Used for the prevention of stroke and systemic embolism in individuals with nonvalvular atrial fibrillation, treatment of deep vein thrombosis (DVT) and pulmonary embolism (PE), and prevention of recurrent VTE.',
    #     #     'warning': 'Requires monitoring of renal function and signs of bleeding, particularly in individuals with renal impairment or a history of bleeding disorders. Should be used with caution in individuals at risk for bleeding or those receiving concomitant medications that increase bleeding risk.',
    #     #     'administration': 'Usually taken orally, with or without food. Tablets should be swallowed whole and not crushed, chewed, or broken.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, as safety data in pregnant individuals is limited. Limited data is available regarding the use of rivaroxaban during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to rivaroxaban or active pathological bleeding, including intracranial, gastrointestinal, or ocular bleeding.'
    #     # },
    #     # {
    #     #     'name': 'Lorazepam',
    #     #     'dosage': 'Dosage varies depending on the indication and individual response. Typically started at 1-2 mg orally, with potential dose adjustments based on the severity of symptoms and tolerability.',
    #     #     'adverse_effects': 'Common side effects include sedation, dizziness, and weakness. May also cause respiratory depression or paradoxical reactions, particularly in elderly individuals.',
    #     #     'indication': 'Used for the management of anxiety disorders, insomnia, and acute alcohol withdrawal symptoms. Also used as preanesthetic medication or adjunctive therapy in the treatment of seizures.',
    #     #     'warning': 'May cause dependence and withdrawal symptoms with long-term use, so treatment should be tapered off gradually to minimize withdrawal reactions. Should be used with caution in individuals with a history of substance abuse or dependence.',
    #     #     'administration': 'Usually taken orally, with or without food. Intravenous administration is also possible for acute situations.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the first trimester, due to the risk of fetal harm. Limited data is available regarding the use of lorazepam during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to benzodiazepines or acute narrow-angle glaucoma.'
    #     # },
    #     # {
    #     #     'name': 'Pregabalin',
    #     #     'dosage': 'Dosage varies depending on the indication and individual response. Typically started at 75 mg orally twice daily or 50 mg three times daily, with potential dose adjustments based on efficacy and tolerability.',
    #     #     'adverse_effects': 'Common side effects include dizziness, somnolence, and peripheral edema. May also cause weight gain or ataxia, particularly at higher doses.',
    #     #     'indication': 'Used for the management of neuropathic pain associated with diabetic peripheral neuropathy, postherpetic neuralgia, and fibromyalgia. Also used as adjunctive therapy for partial-onset seizures.',
    #     #     'warning': 'May cause drowsiness and impair cognitive function, so caution should be exercised when driving or operating machinery. Should be tapered off gradually to minimize withdrawal symptoms.',
    #     #     'administration': 'Usually taken orally, with or without food. Dosage adjustments may be necessary in individuals with renal impairment.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy and lactation, as safety data in these populations is limited.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to pregabalin or gabapentin.'
    #     # },
    #     # {
    #     #     'name': 'Rituximab',
    #     #     'dosage': "Dosage varies depending on the indication and patient's weight. Typically administered intravenously at a dose of 375 mg/m ^ 2 once weekly for 4 to 8 doses.",
    #     #     'adverse_effects': 'Common side effects include infusion reactions, fever, chills, and infections. May also cause gastrointestinal disturbances, respiratory symptoms, or hematological abnormalities.',
    #     #     'indication': 'Used for the treatment of non-Hodgkin lymphoma, chronic lymphocytic leukemia, rheumatoid arthritis, and other autoimmune conditions.',
    #     #     'warning': 'Requires close monitoring for signs of infusion reactions, including fever, chills, hypotension, or bronchospasm. Patients should be premedicated with corticosteroids, antihistamines, and acetaminophen to minimize infusion reactions.',
    #     #     'administration': 'Administered intravenously over several hours in a healthcare setting equipped to manage potential infusion reactions.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy unless the potential benefits outweigh the risks. Limited data is available regarding the use of rituximab during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to rituximab or murine proteins. Not recommended for use in individuals with active infections.'
    #     # },
    #     # {
    #     #     'name': 'Apixaban',
    #     #     'dosage': 'Typically initiated at a dose of 5 mg orally twice daily for the treatment of venous thromboembolism (VTE) or stroke prevention in atrial fibrillation. Dose adjustments may be necessary based on renal function or concomitant medications.',
    #     #     'adverse_effects': 'Common side effects include bleeding, particularly gastrointestinal bleeding. May also cause bruising, itching, or headache.',
    #     #     'indication': 'Used for the prevention of stroke and systemic embolism in individuals with nonvalvular atrial fibrillation, treatment of deep vein thrombosis (DVT) and pulmonary embolism (PE), and prevention of recurrent VTE.',
    #     #     'warning': 'Requires monitoring of renal function and signs of bleeding, particularly in individuals with renal impairment or a history of bleeding disorders. Should be used with caution in individuals at risk for bleeding or those receiving concomitant medications that increase bleeding risk.',
    #     #     'administration': 'Usually taken orally, with or without food. Tablets should be swallowed whole and not crushed, chewed, or broken.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy unless the potential benefits outweigh the risks. Limited data is available regarding the use of apixaban during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to apixaban or active pathological bleeding, including intracranial, gastrointestinal, or ocular bleeding.'
    #     # },
    #     # {
    #     #     'name': 'Esomeprazole',
    #     #     'dosage': "Typically prescribed at a dose of 20-40 mg orally once daily for the treatment of gastroesophageal reflux disease (GERD), erosive esophagitis, or peptic ulcers. Dose adjustments may be necessary based on the severity of symptoms or patient's response.",
    #     #     'adverse_effects': 'Common side effects include headache, nausea, and abdominal pain. May also cause diarrhea, flatulence, or dry mouth.',
    #     #     'indication': 'Used for the treatment of GERD, erosive esophagitis, gastric ulcers, duodenal ulcers, and Helicobacter pylori eradication in combination with antibiotics.',
    #     #     'warning': 'Long-term use may increase the risk of Clostridium difficile-associated diarrhea, bone fractures, or hypomagnesemia. Patients should be monitored for signs of vitamin B12 deficiency or hypomagnesemia with prolonged therapy.',
    #     #     'administration': 'Usually taken orally, at least one hour before meals. Capsules should be swallowed whole and not chewed or crushed.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the first trimester, as safety data in pregnant individuals is limited. Limited data is available regarding the use of esomeprazole during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to esomeprazole or other proton pump inhibitors.'
    #     # },
    #     # {
    #     #     'name': 'Trastuzumab',
    #     #     'dosage': "Dosage varies depending on the indication and patient's weight. Typically administered intravenously at a loading dose of 4 mg/kg followed by maintenance doses of 2 mg/kg once weekly or 6 mg/kg once every three weeks.",
    #     #     'adverse_effects': 'Common side effects include infusion reactions, fatigue, and gastrointestinal disturbances. May also cause cardiotoxicity, neutropenia, or hypersensitivity reactions.',
    #     #     'indication': 'Used for the treatment of HER2-positive breast cancer, HER2-positive gastric or gastroesophageal junction adenocarcinoma, and other HER2-positive malignancies.',
    #     #     'warning': 'Requires close monitoring for signs of infusion reactions, including fever, chills, dyspnea, or hypotension. Cardiac function should be monitored regularly due to the risk of cardiotoxicity.',
    #     #     'administration': 'Administered intravenously over several hours in a healthcare setting equipped to manage potential infusion reactions.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy unless the potential benefits outweigh the risks. Limited data is available regarding the use of trastuzumab during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to trastuzumab or murine proteins. Not recommended for use in individuals with preexisting cardiac dysfunction.'
    #     # },
    #     # {
    #     #     'name': 'Loperamide',
    #     #     'dosage': 'Adults: Initial dose of 4 mg (2 capsules or tablets) followed by 2 mg (1 capsule or tablet) after each unformed stool, not exceeding 16 mg/day.',
    #     #     'adverse_effects': 'Common side effects include constipation, abdominal pain, and nausea. Rarely may cause paralytic ileus or toxic megacolon.',
    #     #     'indication': 'Used for the symptomatic relief of acute diarrhea and chronic diarrhea associated with inflammatory bowel disease or irritable bowel syndrome.',
    #     #     'warning': 'Should be used with caution in individuals with acute dysentery, bacterial enterocolitis, or pseudomembranous colitis associated with antibiotic use. Avoid use in individuals with severe hepatic impairment.',
    #     #     'administration': 'Administered orally with or without food. Capsules or tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the first trimester, as safety data in pregnant individuals is limited. Limited data is available regarding the use of loperamide during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to loperamide or those with acute dysentery, bacterial enterocolitis, or pseudomembranous colitis associated with antibiotic use.'
    #     # },
    #     # {
    #     #     'name': 'Domperidone',
    #     #     'dosage': "Typically prescribed at a dose of 10-20 mg orally three to four times daily, before meals and at bedtime. Dose adjustments may be necessary based on patient's response.",
    #     #     'adverse_effects': 'Common side effects include dry mouth, headache, and gastrointestinal disturbances. May also cause drowsiness or galactorrhea.',
    #     #     'indication': 'Used for the relief of symptoms associated with gastrointestinal motility disorders, including nausea, vomiting, bloating, and reflux.',
    #     #     'warning': 'Should be used with caution in individuals with hepatic impairment or those at risk for cardiac arrhythmias. Avoid concomitant use with drugs known to prolong the QT interval or potent CYP3A4 inhibitors.',
    #     #     'administration': 'Administered orally, ideally before meals. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the first trimester, as safety data in pregnant individuals is limited. Limited data is available regarding the use of domperidone during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with known hypersensitivity to domperidone or those with a history of gastrointestinal hemorrhage, mechanical obstruction, or perforation.'
    #     # },
    #     # {
    #     #     'name': 'Naproxen',
    #     #     'dosage': 'Typically initiated at a dose of 250-500 mg orally twice daily, with a maximum daily dose of 1500 mg for short-term use or 1000 mg for long-term use.',
    #     #     'adverse_effects': 'Common side effects include gastrointestinal disturbances, headache, and dizziness. May also cause fluid retention, hypertension, or renal impairment.',
    #     #     'indication': 'Used for the relief of mild to moderate pain, inflammation, and fever associated with conditions such as osteoarthritis, rheumatoid arthritis, and menstrual cramps.',
    #     #     'warning': 'Long-term use may increase the risk of gastrointestinal bleeding, ulceration, or perforation. Should be used with caution in individuals with a history of cardiovascular disease or renal impairment.',
    #     #     'administration': 'Administered orally, with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during the third trimester of pregnancy due to the potential risk of premature closure of the ductus arteriosus. Limited data is available regarding the use of naproxen during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to naproxen or other NSAIDs, those with a history of asthma, urticaria, or allergic-type reactions to aspirin or other NSAIDs.'
    #     # },
    #     # {
    #     #     'name': 'Aceclofenac',
    #     #     'dosage': 'Recommended dose for adults is typically 100 mg twice daily. Dosage may be adjusted based on individual response and tolerability.',
    #     #     'adverse_effects': 'Common side effects include gastrointestinal disturbances, headache, and dizziness. May also cause rash, pruritus, or liver function abnormalities.',
    #     #     'indication': 'Used for the relief of pain and inflammation associated with conditions such as osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis.',
    #     #     'warning': 'Should be used with caution in individuals with a history of peptic ulcer disease, renal impairment, or heart failure. Avoid concomitant use with other NSAIDs or anticoagulants.',
    #     #     'administration': 'Administered orally, preferably with or after meals. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during the third trimester of pregnancy due to the potential risk of premature closure of the ductus arteriosus. Limited data is available regarding the use of aceclofenac during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with hypersensitivity to aceclofenac or other NSAIDs, those with a history of asthma, urticaria, or allergic-type reactions to aspirin or other NSAIDs.'
    #     # },

    #     # {
    #     #     'name': 'Rivastigmine',
    #     #     'dosage': 'Initial dose: 1.5 mg orally twice daily, titrated based on response and tolerability.\nMaintenance dose: 3-6 mg orally twice daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, vomiting, diarrhea, and dizziness. Serious adverse effects may include bradycardia, syncope, or seizures.',
    #     #     'indication': 'Treatment of mild to moderate Alzheimer\'s disease and Parkinson\'s disease dementia.',
    #     #     'warning': 'May cause bradycardia, syncope, or seizures. Use caution in individuals with a history of cardiac conduction abnormalities or epilepsy.',
    #     #     'administration': 'Administered orally with or without food. Capsules or solutions should be swallowed as directed by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of rivastigmine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to rivastigmine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Budesonide',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally, intranasally, or via inhalation at doses ranging from 0.25 mg to 9 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include headache, nausea, and throat irritation. Serious adverse effects may include adrenal suppression, osteoporosis, or glaucoma.',
    #     #     'indication': 'Treatment of asthma, allergic rhinitis, and inflammatory bowel disease.',
    #     #     'warning': 'May cause adrenal suppression, osteoporosis, or glaucoma. Use caution in individuals with a history of systemic corticosteroid use or immunosuppression.',
    #     #     'administration': 'Administered orally, intranasally, or via inhalation. Follow specific dosing instructions provided by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of budesonide during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to budesonide or other corticosteroids.'
    #     # },
    #     # {
    #     #     'name': 'Olanzapine',
    #     #     'dosage': 'Initial dose: 5-10 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 10-20 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, sedation, and dry mouth. Serious adverse effects may include metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of olanzapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to olanzapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Clonazepam',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally at doses ranging from 0.25 mg to 2 mg 2-3 times daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and ataxia. Serious adverse effects may include respiratory depression, paradoxical reactions, or suicidal ideation.',
    #     #     'indication': 'Treatment of panic disorder, epilepsy, and essential tremor.',
    #     #     'warning': 'May cause respiratory depression, paradoxical reactions, or suicidal ideation. Use caution in individuals with a history of substance abuse or respiratory impairment.',
    #     #     'administration': 'Administered orally. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the first trimester. Limited data is available regarding the safety of clonazepam during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to clonazepam or other benzodiazepines.'
    #     # },
    #     # {
    #     #     'name': 'Risperidone',
    #     #     'dosage': 'Initial dose: 0.5-1 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 1-6 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, sedation, and extrapyramidal symptoms. Serious adverse effects may include hyperprolactinemia, neuroleptic malignant syndrome, or QT prolongation.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and irritability associated with autism.',
    #     #     'warning': 'May cause hyperprolactinemia, neuroleptic malignant syndrome, or QT prolongation. Use caution in individuals with a history of cardiovascular disease or seizure disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of risperidone during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to risperidone or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Mirtazapine',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically initiated at low doses and titrated slowly to target dose, ranging from 15 mg to 45 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, weight gain, and dry mouth. Serious adverse effects may include serotonin syndrome, agranulocytosis, or hepatotoxicity.',
    #     #     'indication': 'Treatment of major depressive disorder and generalized anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, agranulocytosis, or hepatotoxicity. Use caution in individuals with a history of substance abuse or liver disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of mirtazapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to mirtazapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Quetiapine',
    #     #     'dosage': 'Initial dose: 25 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 150-800 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and dry mouth. Serious adverse effects may include metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of quetiapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to quetiapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Lamotrigine',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically initiated at low doses and titrated slowly to target dose, ranging from 25 mg to 200 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include headache, dizziness, and nausea. Serious adverse effects may include Stevens-Johnson syndrome, toxic epidermal necrolysis, or aseptic meningitis.',
    #     #     'indication': 'Treatment of epilepsy, bipolar disorder, and migraine prophylaxis.',
    #     #     'warning': 'May cause Stevens-Johnson syndrome, toxic epidermal necrolysis, or aseptic meningitis. Use caution in individuals with a history of rash or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of lamotrigine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to lamotrigine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Trazodone',
    #     #     'dosage': 'Initial dose: 150 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 150-400 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and dry mouth. Serious adverse effects may include priapism, serotonin syndrome, or orthostatic hypotension.',
    #     #     'indication': 'Treatment of major depressive disorder and insomnia.',
    #     #     'warning': 'May cause priapism, serotonin syndrome, or orthostatic hypotension. Use caution in individuals with a history of cardiovascular disease or hypotension.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of trazodone during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to trazodone or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Venlafaxine',
    #     #     'dosage': 'Initial dose: 75 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 75-225 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, headache, and dry mouth. Serious adverse effects may include serotonin syndrome, hypertension, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and social anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, hypertension, or suicidal ideation. Use caution in individuals with a history of cardiovascular disease or bipolar disorder.',
    #     #     'administration': 'Administered orally with food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of venlafaxine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to venlafaxine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Aripiprazole',
    #     #     'dosage': 'Initial dose: 10-15 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 10-30 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, headache, and akathisia. Serious adverse effects may include neuroleptic malignant syndrome, tardive dyskinesia, or suicidal ideation.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause neuroleptic malignant syndrome, tardive dyskinesia, or suicidal ideation. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of aripiprazole during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to aripiprazole or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Atomoxetine',
    #     #     'dosage': 'Initial dose: 40 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 40-100 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include insomnia, decreased appetite, and dry mouth. Serious adverse effects may include hepatotoxicity, suicidal ideation, or priapism.',
    #     #     'indication': 'Treatment of attention deficit hyperactivity disorder (ADHD) in children, adolescents, and adults.',
    #     #     'warning': 'May cause hepatotoxicity, suicidal ideation, or priapism. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of atomoxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to atomoxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Duloxetine',
    #     #     'dosage': 'Initial dose: 30 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 60-120 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, dry mouth, and constipation. Serious adverse effects may include serotonin syndrome, hepatotoxicity, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and diabetic peripheral neuropathic pain.',
    #     #     'warning': 'May cause serotonin syndrome, hepatotoxicity, or suicidal ideation. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of duloxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to duloxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Sertraline',
    #     #     'dosage': 'Initial dose: 50 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 50-200 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, diarrhea, and insomnia. Serious adverse effects may include serotonin syndrome, hyponatremia, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, obsessive-compulsive disorder, and panic disorder.',
    #     #     'warning': 'May cause serotonin syndrome, hyponatremia, or suicidal ideation. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of sertraline during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to sertraline or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Lisinopril',
    #     #     'dosage': 'Initial dose: 5-10 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 20-40 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include cough, dizziness, and hypotension. Serious adverse effects may include angioedema, hyperkalemia, or renal failure.',
    #     #     'indication': 'Treatment of hypertension, heart failure, and diabetic nephropathy.',
    #     #     'warning': 'May cause angioedema, hyperkalemia, or renal failure. Use caution in individuals with a history of kidney disease or dehydration.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of lisinopril during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to lisinopril or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Paroxetine',
    #     #     'dosage': 'Initial dose: 20 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 20-50 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include drowsiness, dry mouth, and sexual dysfunction. Serious adverse effects may include serotonin syndrome, suicidal ideation, or hyponatremia.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and social anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, suicidal ideation, or hyponatremia. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of paroxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to paroxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Diazepam',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally, intravenously, or rectally at doses ranging from 2 mg to 10 mg 2-4 times daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and ataxia. Serious adverse effects may include respiratory depression, paradoxical reactions, or dependence.',
    #     #     'indication': 'Treatment of anxiety disorders, alcohol withdrawal, and muscle spasms.',
    #     #     'warning': 'May cause respiratory depression, paradoxical reactions, or dependence. Use caution in individuals with a history of substance abuse or respiratory impairment.',
    #     #     'administration': 'Administered orally, intravenously, or rectally. Follow specific dosing instructions provided by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the first trimester. Limited data is available regarding the safety of diazepam during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to diazepam or other benzodiazepines.'
    #     # },
    #     # {
    #     #     'name': 'Rivastigmine',
    #     #     'dosage': 'Initial dose: 1.5 mg orally twice daily, titrated based on response and tolerability.\nMaintenance dose: 3-6 mg orally twice daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, vomiting, diarrhea, and dizziness. Serious adverse effects may include bradycardia, syncope, or seizures.',
    #     #     'indication': 'Treatment of mild to moderate Alzheimer\'s disease and Parkinson\'s disease dementia.',
    #     #     'warning': 'May cause bradycardia, syncope, or seizures. Use caution in individuals with a history of cardiac conduction abnormalities or epilepsy.',
    #     #     'administration': 'Administered orally with or without food. Capsules or solutions should be swallowed as directed by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of rivastigmine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to rivastigmine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Budesonide',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally, intranasally, or via inhalation at doses ranging from 0.25 mg to 9 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include headache, nausea, and throat irritation. Serious adverse effects may include adrenal suppression, osteoporosis, or glaucoma.',
    #     #     'indication': 'Treatment of asthma, allergic rhinitis, and inflammatory bowel disease.',
    #     #     'warning': 'May cause adrenal suppression, osteoporosis, or glaucoma. Use caution in individuals with a history of systemic corticosteroid use or immunosuppression.',
    #     #     'administration': 'Administered orally, intranasally, or via inhalation. Follow specific dosing instructions provided by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of budesonide during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to budesonide or other corticosteroids.'
    #     # },
    #     # {
    #     #     'name': 'Olanzapine',
    #     #     'dosage': 'Initial dose: 5-10 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 10-20 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, sedation, and dry mouth. Serious adverse effects may include metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of olanzapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to olanzapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Clonazepam',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally at doses ranging from 0.25 mg to 2 mg 2-3 times daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and ataxia. Serious adverse effects may include respiratory depression, paradoxical reactions, or suicidal ideation.',
    #     #     'indication': 'Treatment of panic disorder, epilepsy, and essential tremor.',
    #     #     'warning': 'May cause respiratory depression, paradoxical reactions, or suicidal ideation. Use caution in individuals with a history of substance abuse or respiratory impairment.',
    #     #     'administration': 'Administered orally. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the first trimester. Limited data is available regarding the safety of clonazepam during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to clonazepam or other benzodiazepines.'
    #     # },
    #     # {
    #     #     'name': 'Risperidone',
    #     #     'dosage': 'Initial dose: 0.5-1 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 1-6 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, sedation, and extrapyramidal symptoms. Serious adverse effects may include hyperprolactinemia, neuroleptic malignant syndrome, or QT prolongation.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and irritability associated with autism.',
    #     #     'warning': 'May cause hyperprolactinemia, neuroleptic malignant syndrome, or QT prolongation. Use caution in individuals with a history of cardiovascular disease or seizure disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of risperidone during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to risperidone or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Mirtazapine',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically initiated at low doses and titrated slowly to target dose, ranging from 15 mg to 45 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, weight gain, and dry mouth. Serious adverse effects may include serotonin syndrome, agranulocytosis, or hepatotoxicity.',
    #     #     'indication': 'Treatment of major depressive disorder and generalized anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, agranulocytosis, or hepatotoxicity. Use caution in individuals with a history of substance abuse or liver disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of mirtazapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to mirtazapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Quetiapine',
    #     #     'dosage': 'Initial dose: 25 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 150-800 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and dry mouth. Serious adverse effects may include metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause metabolic syndrome, neuroleptic malignant syndrome, or tardive dyskinesia. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of quetiapine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to quetiapine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Lamotrigine',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically initiated at low doses and titrated slowly to target dose, ranging from 25 mg to 200 mg daily.',
    #     #     'adverse_effects': 'Common adverse effects include headache, dizziness, and nausea. Serious adverse effects may include Stevens-Johnson syndrome, toxic epidermal necrolysis, or aseptic meningitis.',
    #     #     'indication': 'Treatment of epilepsy, bipolar disorder, and migraine prophylaxis.',
    #     #     'warning': 'May cause Stevens-Johnson syndrome, toxic epidermal necrolysis, or aseptic meningitis. Use caution in individuals with a history of rash or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of lamotrigine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to lamotrigine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Trazodone',
    #     #     'dosage': 'Initial dose: 150 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 150-400 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and dry mouth. Serious adverse effects may include priapism, serotonin syndrome, or orthostatic hypotension.',
    #     #     'indication': 'Treatment of major depressive disorder and insomnia.',
    #     #     'warning': 'May cause priapism, serotonin syndrome, or orthostatic hypotension. Use caution in individuals with a history of cardiovascular disease or hypotension.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of trazodone during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to trazodone or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Venlafaxine',
    #     #     'dosage': 'Initial dose: 75 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 75-225 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, headache, and dry mouth. Serious adverse effects may include serotonin syndrome, hypertension, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and social anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, hypertension, or suicidal ideation. Use caution in individuals with a history of cardiovascular disease or bipolar disorder.',
    #     #     'administration': 'Administered orally with food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of venlafaxine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to venlafaxine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Aripiprazole',
    #     #     'dosage': 'Initial dose: 10-15 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 10-30 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include weight gain, headache, and akathisia. Serious adverse effects may include neuroleptic malignant syndrome, tardive dyskinesia, or suicidal ideation.',
    #     #     'indication': 'Treatment of schizophrenia, bipolar disorder, and major depressive disorder.',
    #     #     'warning': 'May cause neuroleptic malignant syndrome, tardive dyskinesia, or suicidal ideation. Use caution in individuals with a history of diabetes or cardiovascular disease.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of aripiprazole during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to aripiprazole or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Atomoxetine',
    #     #     'dosage': 'Initial dose: 40 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 40-100 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include insomnia, decreased appetite, and dry mouth. Serious adverse effects may include hepatotoxicity, suicidal ideation, or priapism.',
    #     #     'indication': 'Treatment of attention deficit hyperactivity disorder (ADHD) in children, adolescents, and adults.',
    #     #     'warning': 'May cause hepatotoxicity, suicidal ideation, or priapism. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of atomoxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to atomoxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Duloxetine',
    #     #     'dosage': 'Initial dose: 30 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 60-120 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, dry mouth, and constipation. Serious adverse effects may include serotonin syndrome, hepatotoxicity, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and diabetic peripheral neuropathic pain.',
    #     #     'warning': 'May cause serotonin syndrome, hepatotoxicity, or suicidal ideation. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Capsules should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of duloxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to duloxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Sertraline',
    #     #     'dosage': 'Initial dose: 50 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 50-200 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include nausea, diarrhea, and insomnia. Serious adverse effects may include serotonin syndrome, hyponatremia, or suicidal ideation.',
    #     #     'indication': 'Treatment of major depressive disorder, obsessive-compulsive disorder, and panic disorder.',
    #     #     'warning': 'May cause serotonin syndrome, hyponatremia, or suicidal ideation. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of sertraline during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to sertraline or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Lisinopril',
    #     #     'dosage': 'Initial dose: 5-10 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 20-40 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include cough, dizziness, and hypotension. Serious adverse effects may include angioedema, hyperkalemia, or renal failure.',
    #     #     'indication': 'Treatment of hypertension, heart failure, and diabetic nephropathy.',
    #     #     'warning': 'May cause angioedema, hyperkalemia, or renal failure. Use caution in individuals with a history of kidney disease or dehydration.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the second and third trimesters. Limited data is available regarding the safety of lisinopril during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to lisinopril or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Paroxetine',
    #     #     'dosage': 'Initial dose: 20 mg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 20-50 mg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include drowsiness, dry mouth, and sexual dysfunction. Serious adverse effects may include serotonin syndrome, suicidal ideation, or hyponatremia.',
    #     #     'indication': 'Treatment of major depressive disorder, generalized anxiety disorder, and social anxiety disorder.',
    #     #     'warning': 'May cause serotonin syndrome, suicidal ideation, or hyponatremia. Use caution in individuals with a history of liver disease or mood disorders.',
    #     #     'administration': 'Administered orally with or without food. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the third trimester. Limited data is available regarding the safety of paroxetine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to paroxetine or other components of the formulation.'
    #     # },
    #     # {
    #     #     'name': 'Diazepam',
    #     #     'dosage': 'Dosage regimen varies based on the specific indication, severity of the condition, and patient characteristics. Typically administered orally, intravenously, or rectally at doses ranging from 2 mg to 10 mg 2-4 times daily.',
    #     #     'adverse_effects': 'Common adverse effects include sedation, dizziness, and ataxia. Serious adverse effects may include respiratory depression, paradoxical reactions, or dependence.',
    #     #     'indication': 'Treatment of anxiety disorders, alcohol withdrawal, and muscle spasms.',
    #     #     'warning': 'May cause respiratory depression, paradoxical reactions, or dependence. Use caution in individuals with a history of substance abuse or respiratory impairment.',
    #     #     'administration': 'Administered orally, intravenously, or rectally. Follow specific dosing instructions provided by healthcare provider.',
    #     #     'pregnancy_lactation': 'Should be avoided during pregnancy, especially during the first trimester. Limited data is available regarding the safety of diazepam during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to diazepam or other benzodiazepines.'
    #     # },
    #     # {
    #     #     'name': 'Levothyroxine',
    #     #     'dosage': 'Initial dose: 25-50 mcg orally once daily, titrated based on response and tolerability.\nMaintenance dose: 50-200 mcg orally once daily.',
    #     #     'adverse_effects': 'Common adverse effects include palpitations, weight loss, and insomnia. Serious adverse effects may include tachycardia, arrhythmias, or exacerbation of angina.',
    #     #     'indication': 'Treatment of hypothyroidism and thyroid hormone replacement therapy.',
    #     #     'warning': 'May cause tachycardia, arrhythmias, or exacerbation of angina. Use caution in individuals with a history of cardiovascular disease or adrenal insufficiency.',
    #     #     'administration': 'Administered orally on an empty stomach. Tablets should be swallowed whole with a full glass of water.',
    #     #     'pregnancy_lactation': 'Should be used with caution during pregnancy, especially during the first trimester. Limited data is available regarding the safety of levothyroxine during lactation.',
    #     #     'contraindication': 'Contraindicated in individuals with a history of hypersensitivity to levothyroxine or adrenal insufficiency.'
    #     # }

    # ]

    # drugs = [
    #     {
    #         'name': 'Insulin',
    #         'dosage': 'Dosage varies depending on the type of insulin and individual requirements. Typically administered subcutaneously, with dosing regimens tailored to achieve glycemic control.',
    #         'adverse_effects': 'Common side effects include hypoglycemia, injection site reactions, and weight gain. May also cause allergic reactions or lipodystrophy with prolonged use.',
    #         'indication': 'Used for the treatment of diabetes mellitus to achieve glycemic control and prevent complications associated with hyperglycemia.',
    #         'warning': 'Requires close monitoring of blood glucose levels to adjust dosage and prevent hypoglycemia or hyperglycemia. May interact with many medications, so dosing adjustments may be necessary with changes in medication regimen.',
    #         'administration': 'Administered subcutaneously using insulin syringes or insulin pens. Different formulations may have specific administration instructions.',
    #         'pregnancy_lactation': 'Insulin requirements may change during pregnancy, so regular monitoring of blood glucose levels is essential to maintain glycemic control.',
    #         'contraindication': 'Contraindicated in individuals with hypersensitivity to insulin or components of the formulation.'
    #     },
    #     {
    #         'name': 'Ramipril',
    #         'dosage': 'Typically started at 2.5-5 mg once daily, with potential dose adjustments based on individual response and blood pressure control, for the treatment of hypertension and heart failure.',
    #         'adverse_effects': 'Common side effects include dizziness, cough, and hyperkalemia. May also cause angioedema or renal dysfunction, particularly in individuals with pre-existing kidney disease.',
    #         'indication': 'Used for the treatment of hypertension, heart failure, and prevention of cardiovascular events in individuals at high risk.',
    #         'warning': 'Requires monitoring of blood pressure and renal function, particularly at the initiation of therapy or in individuals at risk for hyperkalemia. Should be used with caution in individuals with a history of angioedema or renal impairment.',
    #         'administration': 'Usually taken orally, with or without food.',
    #         'pregnancy_lactation': 'Should be avoided during pregnancy, especially in the second and third trimesters, due to the risk of fetal harm. Limited data is available regarding the use of ramipril during lactation.',
    #         'contraindication': 'Contraindicated in individuals with a history of angioedema related to previous ACE inhibitor therapy or hereditary angioedema.'
    #     },
    #     {
    #         'name': 'Atenolol',
    #         'dosage': 'Typically started at 25-50 mg once daily, with potential dose adjustments based on individual response and heart rate control, for the treatment of hypertension and angina pectoris.',
    #         'adverse_effects': 'Common side effects include bradycardia, fatigue, and dizziness. May also cause hypotension or exacerbation of heart failure, particularly in individuals with pre-existing cardiovascular disease.',
    #         'indication': 'Used for the treatment of hypertension, angina pectoris, and prevention of cardiovascular events in individuals at high risk.',
    #         'warning': 'May mask symptoms of hypoglycemia in individuals with diabetes mellitus, so caution should be exercised in these populations. Should be used with caution in individuals with bronchospastic diseases due to its potential to exacerbate bronchospasm.',
    #         'administration': 'Usually taken orally, with or without food.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy, especially in the first trimester, as it may cause fetal harm. Limited data is available regarding the use of atenolol during lactation.',
    #         'contraindication': 'Contraindicated in individuals with sinus bradycardia, second or third-degree heart block, cardiogenic shock, or overt heart failure.'
    #     },
    #     {
    #         'name': 'Citalopram',
    #         'dosage': 'Typically started at 20 mg once daily, with potential dose adjustments based on individual response and tolerability, for the treatment of depression and other psychiatric conditions.',
    #         'adverse_effects': 'Common side effects include nausea, dry mouth, and insomnia. May also cause sexual dysfunction or serotonin syndrome, particularly with concomitant use of serotonergic medications.',
    #         'indication': 'Used for the treatment of depression, panic disorder, obsessive-compulsive disorder (OCD), and other psychiatric conditions.',
    #         'warning': 'May increase the risk of suicidal thinking and behavior in children, adolescents, and young adults with major depressive disorder, so close monitoring is necessary during the initial phase of treatment. Should be tapered off gradually to minimize withdrawal symptoms.',
    #         'administration': 'Usually taken orally, with or without food.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy and lactation, as safety data in these populations is limited.',
    #         'contraindication': 'Contraindicated in individuals receiving monoamine oxidase inhibitors (MAOIs) or pimozide due to the risk of serotonin syndrome.'
    #     },
    #     {
    #         'name': 'Gabapentin',
    #         'dosage': 'Dosage varies depending on the indication and individual requirements. Typically started at 300 mg once daily, with gradual titration to achieve optimal dose for the treatment of neuropathic pain or seizures.',
    #         'adverse_effects': 'Common side effects include dizziness, somnolence, and peripheral edema. May also cause weight gain or ataxia, particularly at higher doses.',
    #         'indication': 'Used for the treatment of neuropathic pain, postherpetic neuralgia, and partial-onset seizures.',
    #         'warning': 'May cause drowsiness and impair cognitive function, so caution should be exercised when driving or operating machinery. Should be tapered off gradually to minimize withdrawal symptoms.',
    #         'administration': 'Usually taken orally, with or without food. For individuals with renal impairment, dosage adjustments may be necessary based on creatinine clearance.',
    #         'pregnancy_lactation': 'Should be used with caution during pregnancy and lactation, as safety data in these populations is limited.',
    #         'contraindication': 'Contraindicated in individuals with hypersensitivity to gabapentin or pregabalin.'
    #     }
    # ]
    with transaction.atomic():
        for drug_data in drugs:
            drug = Drug.objects.create(name=drug_data['name'])
            Dosage.objects.create(
                drug=drug, description=drug_data['dosage'])
            AdverseEffect.objects.create(
                drug=drug, description=drug_data['adverse_effects'])
            Indication.objects.create(
                drug=drug, description=drug_data['indication'])
            Warning.objects.create(
                drug=drug, description=drug_data['warning'])
            Administration.objects.create(
                drug=drug, description=drug_data['administration'])
            PregnancyLactation.objects.create(
                drug=drug, description=drug_data['pregnancy_lactation'])
            Contraindication.objects.create(
                drug=drug, description=drug_data['contraindication'])
            print(f"done printing {drug.name}")


if __name__ == "__main__":
    print("Starting drug population script...")
    from medinfo.models import Drug, Dosage, AdverseEffect, Indication, Warning, Administration, PregnancyLactation, Contraindication
    populate_database()
    print("just done populating the")
