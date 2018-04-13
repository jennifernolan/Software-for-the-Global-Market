from modeltranslation.translator import translator, TranslationOptions
from .models import Board
#Indicate what fields translations are nedded for by creating a class
class BoardTranslationOptions(TranslationOptions):
	fields = ('name', 'description',)
#register the translation
translator.register(Board, BoardTranslationOptions)