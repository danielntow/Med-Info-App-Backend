# populate_drug_database.py


import os
import django
from django.db import transaction

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()


@transaction.atomic
def populate_database():

    # Drug 1: Aspirin
    aspirin = Drug.objects.create(name="Aspirin")
    Dosage.objects.create(
        drug=aspirin, description="Typically 325-650 mg every 4 to 6 hours as needed for pain or fever.")
    AdverseEffect.objects.create(
        drug=aspirin, description="Common side effects include stomach irritation, heartburn, and gastrointestinal bleeding.")
    Indication.objects.create(
        drug=aspirin, description="Used for pain relief, fever reduction, and anti-inflammatory purposes.")
    Warning.objects.create(
        drug=aspirin, description="Should be avoided in individuals with bleeding disorders or gastric ulcers.")
    Administration.objects.create(
        drug=aspirin, description="Usually taken orally with a full glass of water.")
    PregnancyLactation.objects.create(
        drug=aspirin, description="Generally considered safe during pregnancy when used in low doses, but should be avoided in the last trimester.")
    Contraindication.objects.create(
        drug=aspirin, description="Should not be used in individuals with bleeding disorders or gastric ulcers.")
    print('u just printed me')

    # Drug 2: Paracetamol
    paracetamol = Drug.objects.create(name="Paracetamol")
    Dosage.objects.create(
        drug=paracetamol, description="Typically 500-1000 mg every 4 to 6 hours as needed for pain or fever.")
    AdverseEffect.objects.create(
        drug=paracetamol, description="Common side effects include liver toxicity, particularly with overdose.")
    Indication.objects.create(
        drug=paracetamol, description="Used for pain relief and fever reduction.")
    Warning.objects.create(
        drug=paracetamol, description="Should not be taken in excessive doses or with alcohol.")
    Administration.objects.create(
        drug=paracetamol, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=paracetamol, description="Generally considered safe during pregnancy when used as directed, but should be used with caution.")
    Contraindication.objects.create(
        drug=paracetamol, description="Should not be taken in excessive doses or with alcohol.")

    # Drug 3: Ibuprofen
    ibuprofen = Drug.objects.create(name="Ibuprofen")
    Dosage.objects.create(
        drug=ibuprofen, description="Typically 200-400 mg every 4 to 6 hours as needed for pain or fever.")
    AdverseEffect.objects.create(
        drug=ibuprofen, description="Common side effects include stomach irritation, heartburn, and gastrointestinal bleeding.")
    Indication.objects.create(
        drug=ibuprofen, description="Used for pain relief, fever reduction, and anti-inflammatory purposes.")
    Warning.objects.create(
        drug=ibuprofen, description="Should be avoided in individuals with a history of stomach ulcers, kidney disease, or cardiovascular disease.")
    Administration.objects.create(
        drug=ibuprofen, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=ibuprofen, description="Should be avoided during the last trimester of pregnancy. Excreted in breast milk, but typically in small amounts.")
    Contraindication.objects.create(
        drug=ibuprofen, description="Should be avoided in individuals with a history of stomach ulcers, kidney disease, or cardiovascular disease.")

    # Drug 4: Loratadine
    loratadine = Drug.objects.create(name="Loratadine")
    Dosage.objects.create(
        drug=loratadine, description="Typically 10 mg once daily for adults and children over 12 years old.")
    AdverseEffect.objects.create(
        drug=loratadine, description="Common side effects include headache, dry mouth, and drowsiness.")
    Indication.objects.create(
        drug=loratadine, description="Used for the relief of symptoms associated with allergic rhinitis (hay fever) and chronic idiopathic urticaria (hives).")
    Warning.objects.create(
        drug=loratadine, description="May cause drowsiness, so caution should be exercised when driving or operating machinery.")
    Administration.objects.create(
        drug=loratadine, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=loratadine, description="Should be used with caution during pregnancy and lactation. Limited data available regarding its safety in these populations.")
    Contraindication.objects.create(
        drug=loratadine, description="Should not be used in individuals with severe liver impairment.")

    # Drug 5: Omeprazole
    omeprazole = Drug.objects.create(name="Omeprazole")
    Dosage.objects.create(
        drug=omeprazole, description="Typically 20-40 mg once daily for the treatment of gastroesophageal reflux disease (GERD) and peptic ulcers.")
    AdverseEffect.objects.create(
        drug=omeprazole, description="Common side effects include headache, diarrhea, and abdominal pain.")
    Indication.objects.create(
        drug=omeprazole, description="Used for the treatment of GERD, peptic ulcers, and other conditions associated with excessive stomach acid production.")
    Warning.objects.create(
        drug=omeprazole, description="Long-term use may increase the risk of Clostridium difficile infection and pneumonia.")
    Administration.objects.create(
        drug=omeprazole, description="Usually taken orally before meals.")
    PregnancyLactation.objects.create(
        drug=omeprazole, description="Generally considered safe during pregnancy and lactation when used as directed.")
    Contraindication.objects.create(
        drug=omeprazole, description="Should be used with caution in individuals with liver impairment.")

    # Drug 6: Simvastatin
    simvastatin = Drug.objects.create(name="Simvastatin")
    Dosage.objects.create(
        drug=simvastatin, description="Typically 10-40 mg once daily for the treatment of high cholesterol levels.")
    AdverseEffect.objects.create(
        drug=simvastatin, description="Common side effects include muscle pain, headache, and gastrointestinal upset.")
    Indication.objects.create(
        drug=simvastatin, description="Used for the treatment of high cholesterol levels (hyperlipidemia) and prevention of cardiovascular events.")
    Warning.objects.create(
        drug=simvastatin, description="May interact with other medications, including certain antibiotics and antifungal agents.")
    Administration.objects.create(
        drug=simvastatin, description="Usually taken orally in the evening.")
    PregnancyLactation.objects.create(
        drug=simvastatin, description="Should not be used during pregnancy or lactation.")
    Contraindication.objects.create(
        drug=simvastatin, description="Should be used with caution in individuals with liver disease or history of muscle disorders.")

    # Drug 7: Metformin
    metformin = Drug.objects.create(name="Metformin")
    Dosage.objects.create(
        drug=metformin, description="Typically started at 500 mg once or twice daily, with gradual titration to a maximum dose of 2000-2500 mg daily for the treatment of type 2 diabetes.")
    AdverseEffect.objects.create(
        drug=metformin, description="Common side effects include gastrointestinal upset, diarrhea, and abdominal discomfort.")
    Indication.objects.create(
        drug=metformin, description="Used for the treatment of type 2 diabetes mellitus.")
    Warning.objects.create(
        drug=metformin, description="Should not be used in individuals with severe kidney impairment or metabolic acidosis.")
    Administration.objects.create(
        drug=metformin, description="Usually taken orally with meals.")
    PregnancyLactation.objects.create(
        drug=metformin, description="Generally considered safe during pregnancy when used as directed.")
    Contraindication.objects.create(
        drug=metformin, description="Should not be used in individuals with severe kidney impairment or metabolic acidosis.")

    # Drug 8: Metoprolol
    metoprolol = Drug.objects.create(name="Metoprolol")
    Dosage.objects.create(
        drug=metoprolol, description="Typically started at 25-50 mg once or twice daily, with gradual titration to a maximum dose of 200-400 mg daily for the treatment of hypertension and angina.")
    AdverseEffect.objects.create(
        drug=metoprolol, description="Common side effects include fatigue, dizziness, and bradycardia (slow heart rate).")
    Indication.objects.create(
        drug=metoprolol, description="Used for the treatment of hypertension, angina, and heart failure.")
    Warning.objects.create(
        drug=metoprolol, description="Should be used with caution in individuals with asthma, COPD, or heart conduction abnormalities.")
    Administration.objects.create(
        drug=metoprolol, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=metoprolol, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=metoprolol, description="Should not be used in individuals with heart block or severe bradycardia.")

    # Drug 9: Sertraline
    sertraline = Drug.objects.create(name="Sertraline")
    Dosage.objects.create(drug=sertraline, description="Typically started at 50 mg once daily, with gradual titration to a maximum dose of 200 mg daily for the treatment of depression, anxiety disorders, and obsessive-compulsive disorder.")
    AdverseEffect.objects.create(
        drug=sertraline, description="Common side effects include nausea, diarrhea, and insomnia.")
    Indication.objects.create(
        drug=sertraline, description="Used for the treatment of major depressive disorder, obsessive-compulsive disorder, and other psychiatric conditions.")
    Warning.objects.create(
        drug=sertraline, description="May increase the risk of suicidal thoughts and behaviors, particularly in children and young adults.")
    Administration.objects.create(
        drug=sertraline, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=sertraline, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=sertraline, description="Should not be used in individuals taking monoamine oxidase inhibitors (MAOIs).")

    # Drug 10: Warfarin
    warfarin = Drug.objects.create(name="Warfarin")
    Dosage.objects.create(
        drug=warfarin, description="Individualized dosing based on international normalized ratio (INR) monitoring, typically 2-10 mg once daily for anticoagulation.")
    AdverseEffect.objects.create(
        drug=warfarin, description="Common side effects include bleeding, bruising, and skin necrosis.")
    Indication.objects.create(
        drug=warfarin, description="Used for the prevention and treatment of thromboembolic disorders such as deep vein thrombosis and atrial fibrillation.")
    Warning.objects.create(
        drug=warfarin, description="Requires regular monitoring of INR levels to maintain therapeutic anticoagulation.")
    Administration.objects.create(
        drug=warfarin, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=warfarin, description="Should be avoided during pregnancy due to the risk of fetal malformations.")
    Contraindication.objects.create(
        drug=warfarin, description="Should not be used in individuals with active bleeding or severe liver disease.")

    # Drug 11: Cetirizine
    cetirizine = Drug.objects.create(name="Cetirizine")
    Dosage.objects.create(
        drug=cetirizine, description="Typically 5-10 mg once daily for the relief of allergy symptoms such as sneezing, itching, and runny nose.")
    AdverseEffect.objects.create(
        drug=cetirizine, description="Common side effects include drowsiness, dry mouth, and headache.")
    Indication.objects.create(
        drug=cetirizine, description="Used for the treatment of allergic rhinitis (hay fever) and chronic idiopathic urticaria (hives).")
    Warning.objects.create(
        drug=cetirizine, description="May cause drowsiness, so caution should be exercised when driving or operating machinery.")
    Administration.objects.create(
        drug=cetirizine, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=cetirizine, description="Should be used with caution during pregnancy and lactation. Limited data available regarding its safety in these populations.")
    Contraindication.objects.create(
        drug=cetirizine, description="Should not be used in individuals with severe liver impairment.")

    # Drug 12: Diazepam
    diazepam = Drug.objects.create(name="Diazepam")
    Dosage.objects.create(
        drug=diazepam, description="Varies depending on the indication, typically starting at 2-10 mg two to four times daily for anxiety or muscle spasms.")
    AdverseEffect.objects.create(
        drug=diazepam, description="Common side effects include drowsiness, dizziness, and confusion.")
    Indication.objects.create(
        drug=diazepam, description="Used for the treatment of anxiety disorders, muscle spasms, and alcohol withdrawal symptoms.")
    Warning.objects.create(
        drug=diazepam, description="May cause drowsiness and impair cognitive function, so caution should be exercised when driving or operating machinery.")
    Administration.objects.create(
        drug=diazepam, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=diazepam, description="Should be avoided during pregnancy due to the risk of fetal abnormalities.")
    Contraindication.objects.create(
        drug=diazepam, description="Should not be used in individuals with a history of substance abuse.")

    # Drug 13: Lisinopril
    lisinopril = Drug.objects.create(name="Lisinopril")
    Dosage.objects.create(
        drug=lisinopril, description="Typically started at 5-10 mg once daily, with gradual titration to a maximum dose of 40 mg daily for the treatment of hypertension and heart failure.")
    AdverseEffect.objects.create(
        drug=lisinopril, description="Common side effects include dizziness, cough, and hyperkalemia.")
    Indication.objects.create(
        drug=lisinopril, description="Used for the treatment of hypertension, heart failure, and prevention of cardiovascular events.")
    Warning.objects.create(
        drug=lisinopril, description="May cause hypotension, particularly in individuals with volume depletion.")
    Administration.objects.create(
        drug=lisinopril, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=lisinopril, description="Should be avoided during pregnancy and lactation, especially during the second and third trimesters.")
    Contraindication.objects.create(
        drug=lisinopril, description="Should not be used in individuals with a history of angioedema related to previous ACE inhibitor therapy.")

    # Drug 14: Levothyroxine
    levothyroxine = Drug.objects.create(name="Levothyroxine")
    Dosage.objects.create(
        drug=levothyroxine, description="Individualized dosing based on thyroid function tests, typically starting at 25-50 mcg once daily for the treatment of hypothyroidism.")
    AdverseEffect.objects.create(
        drug=levothyroxine, description="Common side effects include palpitations, tremors, and insomnia.")
    Indication.objects.create(
        drug=levothyroxine, description="Used for the treatment of hypothyroidism and suppression of thyroid stimulating hormone (TSH) in thyroid cancer.")
    Warning.objects.create(
        drug=levothyroxine, description="Requires careful monitoring of thyroid function tests to adjust dosage.")
    Administration.objects.create(
        drug=levothyroxine, description="Usually taken orally on an empty stomach.")
    PregnancyLactation.objects.create(
        drug=levothyroxine, description="Dosage requirements may increase during pregnancy, so close monitoring is necessary.")
    Contraindication.objects.create(
        drug=levothyroxine, description="Should not be used in individuals with thyrotoxicosis or uncorrected adrenal insufficiency.")

    # Drug 15: Ciprofloxacin
    ciprofloxacin = Drug.objects.create(name="Ciprofloxacin")
    Dosage.objects.create(
        drug=ciprofloxacin, description="Varies depending on the indication, typically starting at 250-750 mg every 12 hours for bacterial infections.")
    AdverseEffect.objects.create(
        drug=ciprofloxacin, description="Common side effects include nausea, diarrhea, and headache. Serious side effects may include tendon rupture and Clostridium difficile-associated diarrhea.")
    Indication.objects.create(
        drug=ciprofloxacin, description="Used for the treatment of bacterial infections including urinary tract infections, respiratory infections, and skin infections.")
    Warning.objects.create(
        drug=ciprofloxacin, description="May increase the risk of tendonitis and tendon rupture, particularly in older adults.")
    Administration.objects.create(
        drug=ciprofloxacin, description="Usually taken orally with water. Can also be administered intravenously.")
    PregnancyLactation.objects.create(
        drug=ciprofloxacin, description="Should be avoided during pregnancy due to the risk of fetal harm.")
    Contraindication.objects.create(
        drug=ciprofloxacin, description="Should not be used in individuals with a history of tendon disorders related to fluoroquinolone use.")

    # Drug 16: Amoxicillin
    amoxicillin = Drug.objects.create(name="Amoxicillin")
    Dosage.objects.create(
        drug=amoxicillin, description="Varies depending on the indication, typically starting at 250-500 mg every 8 hours for bacterial infections.")
    AdverseEffect.objects.create(
        drug=amoxicillin, description="Common side effects include nausea, diarrhea, and rash.")
    Indication.objects.create(
        drug=amoxicillin, description="Used for the treatment of bacterial infections including respiratory tract infections, urinary tract infections, and skin infections.")
    Warning.objects.create(
        drug=amoxicillin, description="May cause allergic reactions, particularly in individuals with a history of penicillin allergy.")
    Administration.objects.create(
        drug=amoxicillin, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=amoxicillin, description="Generally considered safe during pregnancy when used as directed.")
    Contraindication.objects.create(
        drug=amoxicillin, description="Should not be used in individuals with a history of severe allergic reactions to penicillins or cephalosporins.")

    # Drug 17: Atorvastatin
    atorvastatin = Drug.objects.create(name="Atorvastatin")
    Dosage.objects.create(
        drug=atorvastatin, description="Typically 10-80 mg once daily for the treatment of high cholesterol levels.")
    AdverseEffect.objects.create(
        drug=atorvastatin, description="Common side effects include muscle pain, headache, and gastrointestinal upset.")
    Indication.objects.create(
        drug=atorvastatin, description="Used for the treatment of high cholesterol levels (hyperlipidemia) and prevention of cardiovascular events.")
    Warning.objects.create(
        drug=atorvastatin, description="May interact with other medications, including certain antibiotics and antifungal agents.")
    Administration.objects.create(
        drug=atorvastatin, description="Usually taken orally in the evening.")
    PregnancyLactation.objects.create(
        drug=atorvastatin, description="Should not be used during pregnancy or lactation.")
    Contraindication.objects.create(
        drug=atorvastatin, description="Should be used with caution in individuals with liver disease or history of muscle disorders.")

    # Drug 18: Amlodipine
    amlodipine = Drug.objects.create(name="Amlodipine")
    Dosage.objects.create(
        drug=amlodipine, description="Typically started at 5-10 mg once daily for the treatment of hypertension and angina.")
    AdverseEffect.objects.create(
        drug=amlodipine, description="Common side effects include peripheral edema, dizziness, and flushing.")
    Indication.objects.create(
        drug=amlodipine, description="Used for the treatment of hypertension and chronic stable angina.")
    Warning.objects.create(
        drug=amlodipine, description="May cause peripheral edema, particularly in individuals with heart failure.")
    Administration.objects.create(
        drug=amlodipine, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=amlodipine, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=amlodipine, description="Should not be used in individuals with severe aortic stenosis.")

    # Drug 19: Metronidazole
    metronidazole = Drug.objects.create(name="Metronidazole")
    Dosage.objects.create(
        drug=metronidazole, description="Varies depending on the indication, typically starting at 500 mg every 8 hours for bacterial infections.")
    AdverseEffect.objects.create(
        drug=metronidazole, description="Common side effects include nausea, metallic taste, and headache. Serious side effects may include peripheral neuropathy and Clostridium difficile-associated diarrhea.")
    Indication.objects.create(
        drug=metronidazole, description="Used for the treatment of bacterial and protozoal infections including trichomoniasis, giardiasis, and bacterial vaginosis.")
    Warning.objects.create(
        drug=metronidazole, description="Should be avoided in individuals with a history of alcoholism or disulfiram-like reactions. May interact with certain medications including warfarin.")
    Administration.objects.create(
        drug=metronidazole, description="Usually taken orally with water. Available in tablet and liquid formulations, as well as vaginal gel and cream.")
    PregnancyLactation.objects.create(
        drug=metronidazole, description="Should be used with caution during pregnancy and lactation, particularly during the first trimester.")
    Contraindication.objects.create(
        drug=metronidazole, description="Should not be used in individuals with a history of hypersensitivity to nitroimidazole derivatives.")

    # Drug 20: Metoclopramide
    metoclopramide = Drug.objects.create(name="Metoclopramide")
    Dosage.objects.create(
        drug=metoclopramide, description="Varies depending on the indication, typically starting at 10-15 mg three to four times daily for gastrointestinal motility disorders.")
    AdverseEffect.objects.create(
        drug=metoclopramide, description="Common side effects include drowsiness, restlessness, and extrapyramidal symptoms.")
    Indication.objects.create(
        drug=metoclopramide, description="Used for the treatment of gastroesophageal reflux disease (GERD), diabetic gastroparesis, and nausea/vomiting.")
    Warning.objects.create(
        drug=metoclopramide, description="May cause extrapyramidal symptoms, particularly in elderly patients.")
    Administration.objects.create(
        drug=metoclopramide, description="Usually taken orally with water. Can also be administered intravenously.")
    PregnancyLactation.objects.create(
        drug=metoclopramide, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=metoclopramide, description="Should not be used in individuals with a history of gastrointestinal hemorrhage, mechanical obstruction, or perforation.")

    # Drug 21: Fluoxetine
    fluoxetine = Drug.objects.create(name="Fluoxetine")
    Dosage.objects.create(drug=fluoxetine, description="Typically started at 20 mg once daily, with gradual titration to a maximum dose of 80 mg daily for the treatment of depression, obsessive-compulsive disorder, and bulimia nervosa.")
    AdverseEffect.objects.create(
        drug=fluoxetine, description="Common side effects include nausea, insomnia, and headache.")
    Indication.objects.create(
        drug=fluoxetine, description="Used for the treatment of major depressive disorder, obsessive-compulsive disorder, bulimia nervosa, and panic disorder.")
    Warning.objects.create(
        drug=fluoxetine, description="May increase the risk of suicidal thoughts and behaviors, particularly in children and young adults.")
    Administration.objects.create(
        drug=fluoxetine, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=fluoxetine, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=fluoxetine, description="Should not be used in individuals taking monoamine oxidase inhibitors (MAOIs) or thioridazine.")

    # Drug 22: Insulin
    insulin = Drug.objects.create(name="Insulin")
    Dosage.objects.create(
        drug=insulin, description="Individualized dosing based on blood glucose monitoring and insulin sensitivity, typically administered subcutaneously multiple times daily.")
    AdverseEffect.objects.create(
        drug=insulin, description="Common side effects include hypoglycemia and injection site reactions.")
    Indication.objects.create(
        drug=insulin, description="Used for the treatment of diabetes mellitus to control blood glucose levels.")
    Warning.objects.create(
        drug=insulin, description="Requires close monitoring of blood glucose levels to prevent hypoglycemia and hyperglycemia.")
    Administration.objects.create(
        drug=insulin, description="Administered subcutaneously using insulin syringes, pens, or pumps.")
    PregnancyLactation.objects.create(
        drug=insulin, description="Insulin requirements may change during pregnancy, so close monitoring is necessary.")
    Contraindication.objects.create(
        drug=insulin, description="Should not be used in individuals with hypoglycemia unawareness or allergy to any components of the insulin product.")

    # Drug 23: Ramipril
    ramipril = Drug.objects.create(name="Ramipril")
    Dosage.objects.create(
        drug=ramipril, description="Typically started at 2.5-5 mg once daily, with gradual titration to a maximum dose of 10 mg daily for the treatment of hypertension and heart failure.")
    AdverseEffect.objects.create(
        drug=ramipril, description="Common side effects include dizziness, cough, and hyperkalemia.")
    Indication.objects.create(
        drug=ramipril, description="Used for the treatment of hypertension, heart failure, and prevention of cardiovascular events.")
    Warning.objects.create(
        drug=ramipril, description="May cause hypotension, particularly in individuals with volume depletion.")
    Administration.objects.create(
        drug=ramipril, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=ramipril, description="Should be avoided during pregnancy and lactation, especially during the second and third trimesters.")
    Contraindication.objects.create(
        drug=ramipril, description="Should not be used in individuals with a history of angioedema related to previous ACE inhibitor therapy.")

    # Drug 24: Atenolol
    atenolol = Drug.objects.create(name="Atenolol")
    Dosage.objects.create(
        drug=atenolol, description="Typically started at 25-50 mg once daily, with gradual titration to a maximum dose of 100 mg daily for the treatment of hypertension and angina.")
    AdverseEffect.objects.create(
        drug=atenolol, description="Common side effects include fatigue, dizziness, and bradycardia (slow heart rate).")
    Indication.objects.create(
        drug=atenolol, description="Used for the treatment of hypertension and angina.")
    Warning.objects.create(
        drug=atenolol, description="May cause bradycardia and heart block, particularly in individuals with preexisting cardiac conduction abnormalities.")
    Administration.objects.create(
        drug=atenolol, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=atenolol, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=atenolol, description="Should not be used in individuals with sinus bradycardia or heart block greater than first degree.")

    # Drug 25: Citalopram
    citalopram = Drug.objects.create(name="Citalopram")
    Dosage.objects.create(
        drug=citalopram, description="Typically started at 20 mg once daily, with gradual titration to a maximum dose of 40 mg daily for the treatment of depression and anxiety disorders.")
    AdverseEffect.objects.create(
        drug=citalopram, description="Common side effects include nausea, insomnia, and dry mouth.")
    Indication.objects.create(
        drug=citalopram, description="Used for the treatment of major depressive disorder and panic disorder.")
    Warning.objects.create(
        drug=citalopram, description="May increase the risk of suicidal thoughts and behaviors, particularly in children and young adults.")
    Administration.objects.create(
        drug=citalopram, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=citalopram, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=citalopram, description="Should not be used in individuals taking monoamine oxidase inhibitors (MAOIs) or pimozide.")

    # Drug 26: Losartan
    losartan = Drug.objects.create(name="Losartan")
    Dosage.objects.create(
        drug=losartan, description="Typically started at 25-50 mg once daily, with gradual titration to a maximum dose of 100 mg daily for the treatment of hypertension and nephropathy in type 2 diabetes.")
    AdverseEffect.objects.create(
        drug=losartan, description="Common side effects include dizziness, hyperkalemia, and cough.")
    Indication.objects.create(
        drug=losartan, description="Used for the treatment of hypertension and nephropathy in type 2 diabetes.")
    Warning.objects.create(
        drug=losartan, description="May cause hypotension, particularly in individuals with volume depletion.")
    Administration.objects.create(
        drug=losartan, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=losartan, description="Should be avoided during pregnancy and lactation, especially during the second and third trimesters.")
    Contraindication.objects.create(
        drug=losartan, description="Should not be used in individuals with a history of angioedema related to previous ARB therapy.")

    # Drug 27: Aripiprazole
    aripiprazole = Drug.objects.create(name="Aripiprazole")
    Dosage.objects.create(
        drug=aripiprazole, description="Varies depending on the indication, typically starting at 10-15 mg once daily for the treatment of schizophrenia and bipolar disorder.")
    AdverseEffect.objects.create(
        drug=aripiprazole, description="Common side effects include akathisia, insomnia, and weight gain.")
    Indication.objects.create(
        drug=aripiprazole, description="Used for the treatment of schizophrenia, bipolar disorder, and major depressive disorder (as adjunctive therapy).")
    Warning.objects.create(
        drug=aripiprazole, description="May increase the risk of suicidal thoughts and behaviors, particularly in children and young adults.")
    Administration.objects.create(
        drug=aripiprazole, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=aripiprazole, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=aripiprazole, description="Should not be used in individuals with a history of hypersensitivity to aripiprazole or other antipsychotic agents.")

    # Drug 28: Tamsulosin
    tamsulosin = Drug.objects.create(name="Tamsulosin")
    Dosage.objects.create(
        drug=tamsulosin, description="Typically started at 0.4 mg once daily for the treatment of benign prostatic hyperplasia (BPH).")
    AdverseEffect.objects.create(
        drug=tamsulosin, description="Common side effects include dizziness, orthostatic hypotension, and retrograde ejaculation.")
    Indication.objects.create(
        drug=tamsulosin, description="Used for the treatment of benign prostatic hyperplasia (BPH) to improve urinary symptoms.")
    Warning.objects.create(
        drug=tamsulosin, description="May cause orthostatic hypotension, particularly in elderly patients.")
    Administration.objects.create(
        drug=tamsulosin, description="Usually taken orally with water, preferably 30 minutes after the same meal each day.")
    PregnancyLactation.objects.create(
        drug=tamsulosin, description="Not indicated for use in women.")
    Contraindication.objects.create(
        drug=tamsulosin, description="Should not be used in individuals with a history of orthostatic hypotension or severe renal impairment.")

    # Drug 29: Montelukast
    montelukast = Drug.objects.create(name="Montelukast")
    Dosage.objects.create(
        drug=montelukast, description="Typically started at 10 mg once daily for the treatment of asthma and allergic rhinitis.")
    AdverseEffect.objects.create(
        drug=montelukast, description="Common side effects include headache, abdominal pain, and nausea.")
    Indication.objects.create(
        drug=montelukast, description="Used for the treatment of asthma and allergic rhinitis.")
    Warning.objects.create(
        drug=montelukast, description="May cause neuropsychiatric events, including agitation, aggression, and hallucinations, particularly in children.")
    Administration.objects.create(
        drug=montelukast, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=montelukast, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=montelukast, description="Should not be used in individuals with a history of hypersensitivity to montelukast.")

    # Drug 30: Dexamethasone
    dexamethasone = Drug.objects.create(name="Dexamethasone")
    Dosage.objects.create(
        drug=dexamethasone, description="Varies depending on the indication and severity of the condition, typically starting at 0.5-6 mg daily for anti-inflammatory and immunosuppressive effects.")
    AdverseEffect.objects.create(
        drug=dexamethasone, description="Common side effects include insomnia, mood changes, and increased appetite.")
    Indication.objects.create(
        drug=dexamethasone, description="Used for the treatment of inflammatory and autoimmune conditions, allergic reactions, and certain types of cancer.")
    Warning.objects.create(
        drug=dexamethasone, description="Long-term use may increase the risk of osteoporosis, diabetes, and opportunistic infections.")
    Administration.objects.create(
        drug=dexamethasone, description="Usually taken orally with water. Can also be administered intravenously or intramuscularly.")
    PregnancyLactation.objects.create(
        drug=dexamethasone, description="Should be used with caution during pregnancy, particularly during the first trimester.")
    Contraindication.objects.create(
        drug=dexamethasone, description="Should not be used in individuals with systemic fungal infections.")

    # Drug 31: Alprazolam
    alprazolam = Drug.objects.create(name="Alprazolam")
    Dosage.objects.create(
        drug=alprazolam, description="Varies depending on the indication, typically starting at 0.25-0.5 mg three times daily for the treatment of anxiety disorders and panic disorder.")
    AdverseEffect.objects.create(
        drug=alprazolam, description="Common side effects include drowsiness, sedation, and ataxia.")
    Indication.objects.create(
        drug=alprazolam, description="Used for the treatment of anxiety disorders and panic disorder.")
    Warning.objects.create(
        drug=alprazolam, description="May cause dependence and withdrawal symptoms, particularly with long-term use.")
    Administration.objects.create(
        drug=alprazolam, description="Usually taken orally with water.")
    PregnancyLactation.objects.create(
        drug=alprazolam, description="Should be avoided during pregnancy and lactation, especially during the first trimester.")
    Contraindication.objects.create(
        drug=alprazolam, description="Should not be used in individuals with acute narrow-angle glaucoma or hypersensitivity to benzodiazepines.")

    # Drug 32: Venlafaxine
    venlafaxine = Drug.objects.create(name="Venlafaxine")
    Dosage.objects.create(drug=venlafaxine, description="Typically started at 75 mg once daily, with gradual titration to a maximum dose of 375 mg daily for the treatment of depression, generalized anxiety disorder, and social anxiety disorder.")
    AdverseEffect.objects.create(
        drug=venlafaxine, description="Common side effects include nausea, insomnia, and sexual dysfunction.")
    Indication.objects.create(
        drug=venlafaxine, description="Used for the treatment of major depressive disorder, generalized anxiety disorder, and social anxiety disorder.")
    Warning.objects.create(
        drug=venlafaxine, description="May increase the risk of suicidal thoughts and behaviors, particularly in children and young adults.")
    Administration.objects.create(
        drug=venlafaxine, description="Usually taken orally with water, with or without food.")
    PregnancyLactation.objects.create(
        drug=venlafaxine, description="Should be used with caution during pregnancy and lactation.")
    Contraindication.objects.create(
        drug=venlafaxine, description="Should not be used in individuals taking monoamine oxidase inhibitors (MAOIs) or thioridazine.")


if __name__ == "__main__":
    print("Starting drug population script...")
    from medinfo.models import Drug, Dosage, AdverseEffect, Indication, Warning, Administration, PregnancyLactation, Contraindication
    populate_database()
