# %%
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as f

# %%
spark = SparkSession\
    .builder\
    .master('local[*]')\
    .appName('feature engineering')\
    .getOrCreate()

# %%
# Schema do dataset spark
schema = StructType([
    StructField('day_of_purchase', StringType(), False), # será carregado como string para posterior manipulação
    StructField('seller_id', StringType(), False),
    StructField('customer_id', StringType(), False),
    StructField('order_id', StringType(), False),
    StructField('order_status', StringType(), False),
    StructField('order_item_id', IntegerType(), False),
    StructField('product_id', StringType(), False),
    StructField('product_category_name', StringType(), False),
    StructField('price', DoubleType(), False),
    StructField('freight_value', DoubleType(), False),
    StructField('customer_city', StringType(), False),
    StructField('customer_state', StringType(), False),
    StructField('seller_city', StringType(), False),
    StructField('seller_state', StringType(), False)
])

# %%
path_csv = '../../dados/forecast_query.csv'

df = spark.read.csv(
    path_csv,
    inferSchema=True,
    header=True,
    schema=schema
)

# %%
class DataPreparation():
    """
    Classe para preparar os dados para realiazar a feature engineering.
    Caso queria realizar todas as transformações de uma fez, basta acessar
    o método `transform` e ele irá retornar o dataset de treino/teste 
    e validação
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def group_by_date_and_state(self, consolidate=False):
        """
        Agrupa os dados pela data de venda.  
        Para gerar os dataset consolidado (sem separar por estado) mudar
        a variável `consolidadte` = True
        
        """

        self.dataframe = self.dataframe\
            .withColumn(
                'day_of_purchase', 
                f.to_date(self.dataframe['day_of_purchase']))\
            .groupBy('day_of_purchase', 'customer_state')\
            .agg(
                f.sum('price').alias('total_value'),
                f.sum('freight_value').alias('total_freight'),
                f.first('customer_state').alias('customer_state')
            )

        if consolidate == True:
            self.dataframe = self.dataframe\
                .groupBy('day_of_purchase')\
                .agg(
                    f.sum('total_value').alias('total_value'),
                    f.sum('total_freight').alias('total_freight')
                )
        
        
        return self.dataframe
    
    def drop_unnecessary_columns(self):
        columns_to_drop = ['seller_id', 'customer_id', 
                            'order_id', 'order_status', 
                            'order_item_id', 'product_id',
                            'product_category_name', 'customer_city', 
                            'seller_city', 'seller_state']

        self.dataframe = self.dataframe\
            .drop(*(columns_to_drop))

        return self.dataframe

    def split_train_test(self):
        """
        Realizando a separação dos dados entre os dados para treino/modelagem
        e validação. Para o dataset de treino foram considerado o período entre
        janeiro/16 até fev/18 enquanto o de validação o período entre março/18
        até setembro/18
        """

        df = self.dataframe
        df = df.select('*')\
            .where('day_of_purchase > "2016-12-31"')\
            .orderBy('day_of_purchase')

        df_train = df.select('*')\
            .where('day_of_purchase < "2018-03-01"')

        df_validacao = df.select('*')\
            .where('day_of_purchase >= "2018-03-01"')

        df_train = df_train.toPandas().set_index('day_of_purchase')
        df_validacao = df_validacao.toPandas().set_index('day_of_purchase')

        return df_train, df_validacao

    def transform(self, consolidate: bool = False):
        """
        Realiza todas as transformações que estão listadas nessa classe.
        Caso queria discriminar as vedas por estado, manter o parâmetro 
        `consolidate` como False, ou se preferir consolidar tudo, mudar para 
        True
        """
        
        df = self.dataframe

        df = self.group_by_date_and_state(consolidate)
        df = self.drop_unnecessary_columns()
        df_train, df_validacao = self.split_train_test()
        

        return df_train, df_validacao
