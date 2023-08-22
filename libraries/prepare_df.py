import pandas as pd

education_level = pd.read_csv('~/Desktop/sample_panel/data/education_level.csv')
income_group = pd.read_csv('~/Desktop/sample_panel/data/income_group.csv')
procent_pkb = pd.read_excel('~/Desktop/sample_panel/data/procent_pkb_kraje.xlsx')

class PrepareData:

    def pick_frame(self, frame):

        """ Wybierz tabele:
        👉🏼 education_level
        👉🏼 income_group
        👉🏼 procent_pkb
        """

        if frame == 'education_level':
            df_education = education_level.drop(["Flag Codes", "FREQUENCY"], axis=1).fillna(0)
            return df_education

        elif frame == 'income_group':
            df_income = income_group.drop(columns=["SpecialNotes", "Unnamed: 5"], axis=1).fillna(0)
            return df_income

        elif frame == 'procent_pkb':
            df_pkb = procent_pkb.drop(["Indicator Name"], axis=1).fillna(0)
            return df_pkb

        else:
            print('Zła nazwa tabeli ⁉️')