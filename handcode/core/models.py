from django.db import models
from stdimage.models import StdImageField
import uuid

def get_file_path(_instance, filename):
    ex = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ex}'
    return filename

class Worker(models.Model):

    OFFICE = (
        ('Diretor Presidente', 'DPRE'),
        ('Diretor de Markting', 'DMARK'),
        ('Diretor Finaceiro', 'DFIN'),
        ('Diretor de Inovações', 'DINV' ),
        ('Diretor de Gestão de Pessoas', 'DRH'),
        ('Diretor de Projetos', 'DPRJ'),
        ('Desenvolvedor', 'DEV'),
    )

    name = models.CharField('Nome', max_length=100)
    office = models.CharField('Cargo', choices=OFFICE, max_length=30)
    linkdin = models.URLField('Linkedin', max_length=200, blank=True)
    github = models.URLField('GitHub', max_length=200, blank=True)
    instagram = models.URLField('Instagram', max_length=200, blank=True)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height': 480, 'crop': True}})

    class Meta:
        verbose_name = 'Funcionario'

    def __str__(self):
        return self.name
