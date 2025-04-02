import streamlit as st
import pandas as pd
import datetime
import locale
from docxtpl import DocxTemplate
# py -m streamlit run app.py 

st.set_page_config("ΤΕΚΜΗΤΙΩΜΕΝΟ ΑΙΤΗΜΑ", page_icon="🚀", layout="wide")
st.markdown(
    "<h1 style='color: black;'>ΕΦΑΡΜΟΓΗ ΠΑΡΑΓΩΓΗΣ ΑΡΧΕΙΟΥ ΤΕΚΜΗΡΙΩΜΕΝΟΥ ΑΙΤΗΜΑΤΟΣ</h1>", 
    unsafe_allow_html=True
)

# ΑΝΑΓΝΩΣΗ ΑΡΧΕΙΟΥ ΠΡΟΥΠΟΛΟΓΙΣΜΟΥ
@st.cache_data
def load_data():
    return pd.read_excel("pro.xlsx", skiprows=2), pd.read_excel("texniko2024_3_test.xlsx", sheet_name="ΟΛΟΙ ΤΙΜ 26-11-24", skiprows=2, usecols="A, B, D, C")

# Μικροεπεξεργασίες DataFrame
df_pro, df_texniko = load_data() # καλώ την συνάρτηση
df_texniko = df_texniko.iloc[:-1]
df_pro = df_pro.dropna()

tab1, tab2, tab3 = st.tabs(["ΠΡΟΥΠΟΛΟΓΙΣΜΟΣ", "ΤΕΧΝΙΚΟ ΠΡΟΓΡΑΜΜΑ", "ΦΟΡΜΑ ΤΕΚΜΗΡΙΩΜΕΝΟΥ ΑΙΤΗΜΑΤΟΣ"])
with tab1:
     search_value1 = st.text_input("Αναζήτηση ΚΑ")
     search_value2 = st.text_input("Αναζήτηση ΤΙΤΛΟΣ")
     df_pro = df_pro[df_pro['ΚΑ'].astype(str).str.contains(search_value1, case=False, na=False)]
     df_pro = df_pro[df_pro['ΤΙΤΛΟΣ'].astype(str).str.contains(search_value2, case=False, na=False)]
     st.dataframe(df_pro, hide_index=True, width=1700)
     st.metric("Εγγραφές", value=len(df_pro))


with tab2:
     st.dataframe(df_texniko, hide_index=True, width=1700, height=700)

with tab3:
     col1, col2, col3 = st.columns([1.2,3,1])
     # Ορισμός της ελληνικής γλώσσας
     locale.setlocale(locale.LC_TIME, 'el_GR')
     # Ημερομηνία ολόκληρη
     date = datetime.datetime.now().strftime("%d/%m/%Y")    #("%A %d/%m/%Y %H:%M:%S")
     # Πληροφορίες
     plirof = col1.selectbox("Πληροφορίες:", ["Τάνια Γραμματικού", "Κοσμίδης Κοσμάς", "Σάββας Κουγιουμτζόγλου", "Ειρήνη Καρακόλη", "Δημήτριος Παπαναστασίου", "Παύλος Αλεξιάδης"], index=5)
     # Τρέχον οικονομικό έτος
     year = datetime.datetime.now().strftime("%Y")
     #st.write(f"Τρέχον Οικονομικό Έτος: **{year}**")
     # Υπηρεσία
     ypiresia = col1.selectbox("Κωδικός της Διεύθυνσης/Υπηρεσίας του Δήμου:", [10, 20, 30, 40, 45, 50, 55, 60], index=2)
     # Κ.Α.Ε. Προϋπολογισμού
     kae = col2.text_input("Κ.Α.Ε. Προϋπολογισμού:")
     # Τίτλος Κ.Α.Ε
     tkae = col2.text_input("Τίτλος Κ.Α.Ε.:")
     # Αρ. Πρωτ. (ή α.α.) Πρωτoγεvoύς Αιτήματος (με ΑΔΑΜ αν απαιτείται)
     ap = col1.text_input("Αρ. Πρωτ. (ή α.α.) Πρωτoγεvoύς Αιτήματος (με ΑΔΑΜ αν απαιτείται)")
     # Είδος δαπάνης
     idos = col1.radio("Πρόκειται για δαπάνη: ", ["Προμήθειας", "Εργασίας/υπηρεσίας", "Μελέτης", "Έργου", "Μετακίνησης εκτός έδρας"], index=3)
     # Αιτία δαπάνης
     aitia = col2.text_area("Αιτία δαπάνης: ", height=210)


     # Αντιδήμαρχος
     antidimarxos = col1.selectbox("Αντιδήμαρχος που υπογράφει το τεκμηριωμένο αίτημα:", ["ΠΑΥΛΟΣ ΑΛΕΞΙΑΔΗΣ", "ΚΩΝΣΤΑΝΤΙΝΟΣ ΡΟΖΑΣ", "ΑΘΑΝΑΣΙΟΣ ΜΠΕΛΤΣΟΣ", "ΚΩΝΣΤΑΝΤΙΝΟΣ ΒΑΣΙΛΕΙΟΥ"])

     l = ["Η με αρ. 61/2025 (ΑΔΑ: 9ΦΥ1ΩΗΙ-ΟΕΕ) απόφαση Δημάρχου σχετικά με: «Μεταβίβαση αρμοδιότητας και εξουσιοδότηση υπογραφής τεκμηριωμένου αιτήματος».",
          "Η με αρ. 1/2025 (ΑΔΑ: 9ΡΖΤΩΗΙ-ΜΣΟ) απόφαση Δημάρχου σχετικά με: «Ορισμός Αντιδημάρχων και μεταβίβαση αρμοδιοτήτων».",
          "Ο Οργανισμός Εσωτερικής Υπηρεσίας (ΟΕΥ) του Δήμου Φλώρινας (ΦΕΚ 3140Β’/27-11-2012) όπως τροποποιήθηκε και ισχύει.",
          f"Ο εγκεκριμένος προϋπολογισμός του Δήμου Φλώρινας του έτους {year}",
          "Η ανάγκη για εκπροσώπηση του Δήμου για θέματα συμφερόντων και προαγωγής δράσεων του Δήμου.",
          "Η υποχρέωση του υπαλλήλου να προβεί σε παραλαβή του έργου με την επιτροπή παραλαβής στην οποία μετέχει."]

     # Γενικές ή Ειδικές διατάξεις Νόμου στις οποίες βασίζονται οι δαπάνες
     diataxisnomou = col2.multiselect("Γενικές ή Ειδικές διατάξεις Νόμου στις οποίες βασίζονται οι δαπάνες", l, placeholder="Διάλεξε μία ή περισσότερες...")

     # Πηγή Χρηματοδότησης
     pigi = col1.multiselect("Πηγή Χρηματοδότησης:", ["ΣΑΤΑ-ΠΟΕ",
                                                  "ΣΑΤΑ ΣΧΟΛΕΙΩΝ ΠΟΕ",
                                                  "Ε.Α.Π. 2012-2016",
                                                  "ΠΡΑΣΙΝΟ ΤΑΜΕΙΟ",
                                                       "ΠΡΟΓΡΑΜΜΑ ΥΠΟΣΤΗΡΙΞΗΣ ΠΡΑΣΙΝΟΥ ΚΑΙ ΒΙΩΣΙΜΟΥ ΜΕΤΑΣΧΗΜΑΤΙΣΜΟΥ ΤΩΝ ΛΙΓΝΙΤΙΚΩΝ ΠΕΡΙΟΧΩΝ",
                                                       "ΤΑΜΕΙΟ ΑΝΑΚΑΜΨΗΣ",
                                                       "ΦΙΛΟΔΗΜΟΣ ΙΙ",
                                                       "Ε.Π.ΑΝ.Ε.Κ.",
                                                       "ΠΡΟΓΡΑΜΜΑ ΑΝΤΩΝΗΣ ΤΡΙΤΣΗΣ",
                                                       "ΕΙΔΙΚΟ ΠΡΟΓΡΑΜΜΑ ΦΥΣΙΚΩΝ ΚΑΤΑΣΤΡΟΦΩΝ",
                                                       "ΕΠ ΠΔΜ ΔΥΤΙΚΗ ΜΑΚΕΔΟΝΙΑ 2021-2027",
                                                       "ΠΔΕ ΥΠΟΥΡΓΕΙΟΥ ΕΣΩΤΕΡΙΚΩΝ ΣΑΕΠ 041"], placeholder="Διάλεξε μία ή περισσότερες...")

     # Ποσό Δαπάνης (σύνολο)
     poso = col2.number_input("Ποσό Δαπάνης (σύνολο):", value=30000.00, format="%.2f")
     #poso = str(poso).replace(".", ",")
     #col2.text(poso)


     if col2.button("Δημιούργησε αρχείο word", icon="🧾"):
          doc = DocxTemplate("template.docx")
          context = { 'date' : date,
                         'plirof' : plirof,
                         'year' : year,
                         'antidimarxos' : antidimarxos,
                         'ypiresia' : ypiresia,
                         'tkae' : tkae,
                         'kae' : kae,
                         'ap' : ap,
                         'idos' : idos,
                              'aitia' : aitia,
                              'poso' : poso,
                              'pigi' : " - ".join(pigi),
                              'diataxisnomou' : "\n".join(f"{i+1}. {item}" for i, item in enumerate(diataxisnomou)) }
          doc.render(context)
          doc.save(f"ΤΕΚΜΗΡΙΩΜΕΝΟ ΑΙΤΗΜΑ {tkae[:31]}.docx")
          col2.success("Το αρχείο δημιουργήθηκε επιτυχώς")    
