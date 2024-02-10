# Melhorar o código para manipular o banco de dados sqlite3

import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

__login__obj = __login__(auth_token = "courier_auth_token",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

def main():
    st.image('public/images/IBGE.svg', width=400)
    st.header('Um jeito simples de visualizar e analisar seus dados')
    file = st.file_uploader('Escolha a base de dados CSV', type='csv')
    if file is not None:
        try:
            try:
                data = pd.read_csv(file)
            except UnicodeDecodeError:
                data = pd.read_csv(file, encoding='ISO-8859-1')
            except pd.errors.ParserError:
                data = pd.read_csv(file, delimiter=';')

            st.sidebar.header("Envio de e-mail")
            st.sidebar.image('public/images/IBGE.svg')
            columns = st.slider('Quantas colunas deseja ver?', min_value=1, max_value=50)
            st.markdown('**SEU DATAFRAME**:')
            st.dataframe(data.head(columns))

            if st.sidebar.checkbox('Quero visualizar meus dados com Plotly'):
                columns_names = filtered_data.columns.tolist()
                x_axis = st.sidebar.selectbox('Escolha a coluna para o eixo X com Plotly', columns_names)
                y_axis = st.sidebar.selectbox('Escolha a coluna para o eixo Y com Plotly', columns_names, index=1)
                fig = px.scatter(data_frame=filtered_data, x=x_axis, y=y_axis)
                st.plotly_chart(fig)

            if st.sidebar.checkbox('Quero ver o shape dos meus dados'):
                st.markdown('**Quantidade de linhas:** ')
                st.markdown(data.shape[0])
                st.markdown('**Quantidade de colunas:**')
                st.markdown(data.shape[1])

            if st.sidebar.checkbox('Quero analisar as colunas'):
                all_columns = data.columns.tolist()
                selected_columns = st.multiselect('Selecione', all_columns)
                new_df = data[selected_columns]
                st.dataframe(new_df)

            if st.sidebar.checkbox('Quero contar a quantidade de target/classes'):
                st.markdown('**Contagem de Alvos/Classes**')
                st.write(data.iloc[:, -1].value_counts())

            if st.sidebar.checkbox('Quero ver os tipos dos dados'):
                st.markdown('**Tipos de dados**')
                st.write(data.dtypes)

            if st.sidebar.checkbox('Quero a descrição dos meus dados'):
                st.markdown('**Descrição**')
                st.write(data.describe())

            if st.sidebar.checkbox('Quero filtrar meus dados'):
                columns_names = data.columns.tolist()
                selected_column = st.sidebar.selectbox('Escolha a coluna para filtrar', columns_names)
                if data[selected_column].dtype == 'object':
                    filter_values = st.sidebar.multiselect('Escolha o valor', data[selected_column].unique())
                    if filter_values:
                        filtered_data = data[data[selected_column].isin(filter_values)]
                else:
                    min_value, max_value = data[selected_column].min(), data[selected_column].max()
                    value_range = st.sidebar.slider('Escolha um intervalo de valores', min_value, max_value, (min_value, max_value))
                    filtered_data = data[data[selected_column].between(value_range[0], value_range[1])]
                st.dataframe(filtered_data)

            # Gráficos Interativos com Plotly
            if st.sidebar.checkbox('Visualizar Gráfico Interativo'):
                fig = px.scatter(data_frame=filtered_data, x=x_axis, y=y_axis)
                st.plotly_chart(fig)

            if st.sidebar.checkbox('Visualizar Gráfico de Dispersão'):
                st.markdown('**Gráfico de Dispersão**')
                columns_names = data.columns.tolist()
                x_axis = st.sidebar.selectbox('Escolha a coluna para o eixo X', columns_names)
                y_axis = st.sidebar.selectbox('Escolha a coluna para o eixo Y', columns_names, index=1)
                if st.button('Gerar Gráfico de Dispersão'):
                    fig, ax = plt.subplots()
                    ax.scatter(data[x_axis], data[y_axis])
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    st.pyplot(fig)

            if st.sidebar.checkbox('Quero visualizar meus dados'):
                columns_names = data.columns.tolist()
                viz = ('line', 'bar', 'pie', 'hist', 'correlation', 'box', 'scatter')
                selected_plot = st.sidebar.selectbox('Selecione o tipo de visualização', viz)
                selected_columns_names = st.multiselect('Selecione as colunas para o gráfico', columns_names)

                if selected_plot == 'line':
                    custom_data = data[selected_columns_names]
                    st.line_chart(custom_data)
                elif selected_plot == 'bar':
                    custom_data = data[selected_columns_names]
                    st.bar_chart(custom_data)
                elif selected_plot == 'pie':
                    if len(selected_columns_names) > 0:
                        pie_data = data[selected_columns_names[0]].value_counts()
                        plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
                        st.pyplot(plt)
                elif selected_plot == 'correlation':
                    corr = data.corr()
                    st.write(sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True))
                    st.pyplot()
                elif selected_plot == 'box':
                    custom_data = data[selected_columns_names]
                    st.write(sns.boxplot(data=custom_data))
                    st.pyplot()
                elif selected_plot == 'hist':
                    custom_data = data[selected_columns_names]
                    st.write(custom_data.plot(kind='hist', bins=30, alpha=0.5))
                    st.pyplot()
                elif selected_plot == 'scatter':
                    if len(selected_columns_names) >= 2:
                        st.write(sns.scatterplot(data=data, x=selected_columns_names[0], y=selected_columns_names[1]))
                        st.pyplot()

            if st.sidebar.checkbox('Sobre'):
                html = """
                <div style="background-color:indigo;"><p style="color:white;">
                Esse trabalho foi desenvolvido por mim, <a href="https://github.com/estevam5s", 
                style="color:yellow">Estevam Souza</a>, 
                """
                st.markdown(html,  unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__=='__main__':
    if LOGGED_IN == True:
        main()