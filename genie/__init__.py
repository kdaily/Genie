from __future__ import absolute_import
from .example_filetype_format import FileTypeFormat
from .bed import bed
from .bedSP import bedSP
from .workflow import workflow
from .clinical import clinical
from .veoibd_clinical import ClinicalIndividual
from .veoibd_clinical import ClinicalSample
from .veoibd_workflow import Workflow
from .seg import seg
from .cbs import cbs
from .maf import maf
from .mafSP import mafSP
from .clinicalSP import clinicalSP
from .vcf import vcf
from .cna import cna
from .fusions import fusions
from .sampleRetraction import sampleRetraction
from .patientRetraction import patientRetraction
# from .patientCounts import patientCounts
from .mutationsInCis import mutationsInCis
# from .vitalStatus import vitalStatus
from .assay import Assayinfo
from . import process_functions
from . import create_case_lists

PROCESS_FILES = {# 'bed': bed,
                 # 'bedSP': bedSP,
                 # 'maf': maf,
                 # 'mafSP': mafSP,
                 'clinical': clinical,
                 'veoibd_clinical_individual': ClinicalIndividual,
                 'veoibd_clinical_sample': ClinicalSample,
                 'clinicalSP': clinicalSP,
                 'vcf': vcf,
                 # 'cbs': cbs,
                 # 'cna': cna,
                 # 'fusions': fusions,
                 'veoibd_workflow': Workflow,
                 # 'seg': seg,
                 # 'patientRetraction': patientRetraction,
                 # 'sampleRetraction': sampleRetraction,
                 # 'patientCounts': patientCounts,
                 # 'mutationsInCis': mutationsInCis,
                 # 'vitalStatus': vitalStatus,
                 'assayinfo': Assayinfo}

# Must import validate after the fact
from . import input_to_database
from . import validate
from . import toRetract
from . import write_invalid_reasons
# Import logging last to not take in synapseclient logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("genie")
