FROM python:3.7

#set the working directory
WORKDIR /Fampay

#copy the requirements file to the container
COPY requirements.txt .

#Intall the Dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of the project files
COPY . .

#Expose the port 8000
EXPOSE 8000

#Run the Django Server
CMD ["python","manage.py","runserver","0:8000"]