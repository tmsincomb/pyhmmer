import unittest

from pyhmmer.easel import Alphabet
from pyhmmer.errors import UnexpectedError, AllocationError, EaselError, AlphabetMismatch


class TestErrors(unittest.TestCase):

    def test_unexpected_error(self):
        err = UnexpectedError(1, "p7_ReconfigLength")
        self.assertEqual(repr(err), "UnexpectedError(1, 'p7_ReconfigLength')")
        self.assertEqual(str(err), "Unexpected error occurred in 'p7_ReconfigLength': eslFAIL (status code 1)")

    def test_allocation_error(self):
        err = AllocationError("ESL_SQ", 16)
        self.assertEqual(repr(err), "AllocationError('ESL_SQ', 16)")
        self.assertEqual(str(err), "Could not allocate 16 bytes for type ESL_SQ")

        err2 = AllocationError("float", 4, 32)
        self.assertEqual(repr(err2), "AllocationError('float', 4, 32)")
        self.assertEqual(str(err2), "Could not allocate 128 bytes for an array of 32 float")

    def test_easel_error(self):
        err = EaselError(1, "failure")
        self.assertEqual(repr(err), "EaselError(1, 'failure')")
        self.assertEqual(str(err), "Error raised from C code: failure, eslFAIL (status code 1)")

    def test_alphabet_mismatch(self):
        err = AlphabetMismatch(Alphabet.dna(), Alphabet.rna())
        self.assertEqual(repr(err), "AlphabetMismatch(pyhmmer.easel.Alphabet.dna(), pyhmmer.easel.Alphabet.rna())")
        self.assertEqual(str(err), "Expected pyhmmer.easel.Alphabet.dna(), found pyhmmer.easel.Alphabet.rna()")
        self.assertNotEqual(err, 1)

        err2 = AlphabetMismatch(Alphabet.dna(), Alphabet.rna())
        self.assertEqual(err, err)
        self.assertEqual(err, err2)

        err3 = AlphabetMismatch(Alphabet.dna(), Alphabet.amino())
        self.assertNotEqual(err, err3)
