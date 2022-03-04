FROM python:3.10.2
COPY . /usr/ML_Carapp_Streamlit/
EXPOSE 8501
WORKDIR /usr/ML_Carapp_Streamlit/
RUN pip install pip==21.2.4
RUN pip install -r requirements.txt
CMD streamlit run app.py 