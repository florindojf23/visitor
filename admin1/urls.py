from django.urls import path
from .views import *

urlpatterns=[
	path('',home ,name='home'),
	path('funcionariu/',funcionariu, name='funcionariu'),
	path('visitor/',visitor, name='visitor'),
	path('detailvisitor/',detailvisitor, name='detailvisitor'),

	path('create_funcionariu/', createFuncionariu, name="create_funcionariu"),
	path('update_funcionariu/<str:id>', updateFuncionariu, name="update_funcionariu"),
	path('delete_funcionariu/<str:pk>', deleteFuncionariu, name="delete_funcionariu"),

	path('create_visitor/', createvisitor, name="create_visitor"),
	path('update_visitor/<str:id>', updatevisitor, name="update_visitor"),
	path('delete_visitor/<str:pk>', deleteVisitor, name="delete_visitor"),

	path('create_det_visitor/', createdetvisitor, name="create_det_visitor"),
	path('update_det_visitor/<str:id>', updatedetvisitor, name="update_det_visitor"),
	path('delete_det_visitor/<str:id>', deletedetvisitor, name="delete_det_visitor"),

	path('pdf_funcionariu/', pdf_funcionariu, name="pdf_funcionariu"),
	path('csv_funcionariu/', csv_funcionariu, name="csv_funcionariu"),
	path('pdf_visitor/', pdf_visitor, name="pdf_visitor"),
	path('csv_visitor/', csv_visitor, name="csv_visitor"),
	path('pdf_det_visitor/', pdf_det_visitor, name="pdf_det_visitor"),
	path('csv_det_visitor/', csv_det_visitor, name="csv_det_visitor"),

	path('charts/', charts, name="charts"),
	path('chart_seksu_visitor/', chart_seksu_visitor, name="chart_seksu_visitor"),
	path('chart_municipiu_funcionariu/', chart_municipiu_funcionariu, name="chart_municipiu_funcionariu"),

	path('liveFunSave/', liveFunSave, name="liveFunSave"),
	path('liveVisSave/', liveVisSave, name="liveVisSave"),
	
]