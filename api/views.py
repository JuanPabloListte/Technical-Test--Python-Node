from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.core.mail import send_mail
from io import BytesIO
import fitz
from django.conf import settings


class CargarPDFView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        return render(request, 'cargar_pdf.html')

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        email = request.data.get('email')

        if not file or not email:
            return Response({"error": "El PDF y el correo electrónico son requeridos"}, status=status.HTTP_400_BAD_REQUEST)
        
        file_stream = BytesIO(file.read())
        
        try:
            doc = fitz.open(stream=file_stream, filetype="pdf")
            text = ''
            for page in range(len(doc)):
                text += doc[page].get_text()

                if len(text.splitlines()) >= 30:
                    break

            extracted_text = '\n'.join(text.splitlines()[:30])

            send_mail(
                'Texto extraido',
                extracted_text,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({"error": f"Error al procesar el archivo. Verifique sus credenciales de correo electronico."}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"message": f"Se extrajo el texto y se envió al correo electrónico: {email}"}, status=status.HTTP_200_OK)
