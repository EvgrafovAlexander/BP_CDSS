from django.db import models

# Create your models here.


# таблица 1 - общая информация о пациентах
class Patients(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"


# таблица 2 - общий анализ крови
class CompleteBloodCount(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date_cbc = models.DateField('Дата анализа', null=True)
    rbc_cbc = models.DecimalField('Эритроциты, 10^12/л', max_digits=3, decimal_places=3, null=True)
    hb_cbc = models.DecimalField('Гемоглобин, г/л', max_digits=3, decimal_places=3, null=True)
    wbc_cbc = models.DecimalField('Лейкоциты, 10^9/л', max_digits=3, decimal_places=3, null=True)
    mchc_cbc = models.DecimalField('Цветовой показатель, %', max_digits=3, decimal_places=3, null=True)
    esr_cbc = models.DecimalField('Скорость оседания эритроцитов, мм/ч', max_digits=3, decimal_places=3, null=True)
    eos_cbc = models.DecimalField('Эозинофилы, %', max_digits=3, decimal_places=3, null=True)
    stab_cbc = models.DecimalField('Палочкоядерные, %', max_digits=3, decimal_places=3, null=True)
    segm_cbc = models.DecimalField('Сегментоядерные, %', max_digits=3, decimal_places=3, null=True)
    lym_cbc = models.DecimalField('Лимфоциты, %', max_digits=3, decimal_places=3, null=True)
    mon_cbc = models.DecimalField('Моноциты, %', max_digits=3, decimal_places=3, null=True)
    bas_cbc = models.DecimalField('Базофилы, %', max_digits=3, decimal_places=3, null=True)
    rpr_cbc = models.CharField('Микрореакция', max_length=50, null=True)
    young_cbc = models.DecimalField('Юные нейтрофилы, %', max_digits=3, decimal_places=3, null=True)

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = "Общий анализ крови"
        verbose_name_plural = "Общие анализы крови"


# таблица 3 - общий анализ мочи
class ClinicalUrineTest(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date_cut = models.DateField('Дата анализа', null=True)
    col_cut = models.CharField('Цвет', max_length=50, null=True)
    ph_cut = models.DecimalField('Кислотность', max_digits=3, decimal_places=3, null=True)
    sg_cut = models.DecimalField('Удельный вес', max_digits=4, decimal_places=2, null=True)
    transp_cut = models.CharField('Прозрачность', max_length=50, null=True)
    pro_cut = models.CharField('Белок', max_length=50, null=True)
    epith_cut = models.CharField('Эпителий', max_length=50, null=True)
    wbc_cut = models.CharField('Лейкоциты', max_length=50, null=True)
    rbc_cut = models.CharField('Эритроциты', max_length=50, null=True)
    salt_cut = models.CharField('Соли', max_length=50, null=True)
    bact_cut = models.CharField('Бактерии', max_length=50, null=True)

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = "Общий анализ мочи"
        verbose_name_plural = "Общие анализы мочи"


# таблица 4 - биохимический анализ крови
class BiochemicalBloodAnalysis(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date_bba = models.DateField('Дата анализа', null=True)
    total_pro_bba = models.DecimalField('Общий белок', max_digits=3, decimal_places=2, null=True)
    creatin_bba = models.DecimalField('Креатинин', max_digits=3, decimal_places=2, null=True)
    urea_bba = models.DecimalField('Мочевина', max_digits=3, decimal_places=2, null=True)
    total_bil_bba = models.DecimalField('Общий билирубин', max_digits=3, decimal_places=2, null=True)
    cholest_bba = models.DecimalField('Холестирин', max_digits=3, decimal_places=2, null=True)
    alt_bba = models.DecimalField('Аланинаминотрансфераза', max_digits=3, decimal_places=2, null=True)
    ast_bba = models.DecimalField('Аспартатаминотрансфераза', max_digits=3, decimal_places=2, null=True)
    crp_bba = models.DecimalField('С-реактивный протеин', max_digits=3, decimal_places=2, null=True)
    potassium_bba = models.DecimalField('Калий', max_digits=3, decimal_places=2, null=True)
    natr_bba = models.DecimalField('Натрий', max_digits=3, decimal_places=2, null=True)
    not_data_bba = models.DecimalField('Пустая колонка', max_digits=3, decimal_places=2, null=True)

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = "Биохимический анализ крови"
        verbose_name_plural = "Биохимические анализы крови"


# таблица 5 - коагулограмма
class CoagulogramTest(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date_cgt = models.DateField('Дата анализа', null=True)
    apt_time_cgt = models.DecimalField('АЧТВ', max_digits=3, decimal_places=2, null=True)
    ina_cgt = models.DecimalField('МНО', max_digits=3, decimal_places=2, null=True)
    prot_index_cgt = models.DecimalField('ПТИ', max_digits=3, decimal_places=2, null=True)
    fibrin_cgt = models.DecimalField('Фибрин', max_digits=3, decimal_places=2, null=True)
    not_data_cgt = models.DecimalField('Пустая колонка', max_digits=3, decimal_places=2, null=True)

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = "Коагулограмма"
        verbose_name_plural = "Коагулограммы"


# таблица 6 - общий анализ мокроты
class SputumTest(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date_stt = models.DateField('Дата анализа', null=True)
    color_stt = models.CharField('Цвет', max_length=50, null=True)
    nature_stt = models.CharField('Характер', max_length=50, null=True)
    consistency_stt = models.CharField('Консистенция', max_length=50, null=True)
    wbc_stt = models.CharField('Лейкоциты', max_length=50, null=True)
    rbc_stt = models.CharField('Эритроциты', max_length=50, null=True)
    epith_stt = models.CharField('Эпителий', max_length=50, null=True)
    alveolar_stt = models.CharField('Альв.макрофаги', max_length=50, null=True)
    bact_stt = models.CharField('Бактерии', max_length=50, null=True)
    bact_tub_stt = models.CharField('Бакт.туберкулез', max_length=50, null=True)

    def __str__(self):
        return self.patient

    class Meta:
        verbose_name = "Общий анализ мокроты"
        verbose_name_plural = "Общие анализы мокроты"
