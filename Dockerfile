FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR frontend
ENTRYPOINT [ "python" ]
CMD ["frontend.py" ]
EXPOSE 5000