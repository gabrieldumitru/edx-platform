from import_shims.warn import warn_deprecated_import

warn_deprecated_import('student.tests.test_tasks', 'common.djangoapps.student.tests.test_tasks')

from common.djangoapps.student.tests.test_tasks import *
