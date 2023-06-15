# reading dicom
from pydicom.datadict import dictionary_VR
from pydicom.dataset import Dataset
from pydicom import dcmread
from pydicom.data import get_testdata_file
fpath = get_testdata_file("CT_small.dcm")
ds = dcmread(fpath)
# print(ds)

# reading with with open
# with open(fpath, 'rb') as infile:
#     ds = dcmread(infile)
#     print(ds)

# viewing and accessing
"""
(0008, 0005): The element's tag, as (group number, element number) in hexadecimal
Specific Character Set: the element's name, if known
CS: The element's Value Representation (VR), if known
'ISO_IR_100': the element's stored value
"""
# print(ds)
# elem = ds[0x0008, 0x0016]
# print(elem)
# print(elem.keyword)
# private_elem = ds[0x0043, 0x104e]
# print(private_elem)
# print(private_elem.keyword)
# elem = ds['SOPClassUID']
# print(elem)
# print(elem.value)
# print(ds.SOPClassUID)
# print(ds.ImageType)
# print(ds['ImageType'].VM)
# print(ds.ImageType[1])

# Sequences
# print(ds)
# seq = ds[0x0010, 0x1002]
# seq = ds['OtherPatientIDsSequence']

# print(len(ds.OtherPatientIDsSequence))
# print(type(ds.OtherPatientIDsSequence[0]))
# print(ds.OtherPatientIDsSequence[0])
# print(ds.OtherPatientIDsSequence[1])

# file_meta
# print(ds.preamble)
# print(ds.file_meta)
# print(ds.file_meta.TransferSyntaxUID)
# print(ds.file_meta.TransferSyntaxUID.name)

# Modifying
# Modifying elements
# elem = ds[0x0010, 0x0010]
# print(elem.value)
# elem.value = 'Citizen^Jan'
# print(elem)
# ds.PatientName = 'Citizen^Snips'
# print(elem)
# ds.ImageType = ['ORIGINAL', 'PRIMARY', 'LOCALIZER']
# print(ds.ImageType)
# ds.ImageType[1] = 'DERIVED'
# print(ds.ImageType)
# ds.ImageType.insert(1, 'PRIMARY')
# print(ds.ImageType)

# ds.OtherPatientIDsSequence = [Dataset(), Dataset()]
# ds.OtherPatientIDsSequence.append(Dataset())
# print(len(ds.OtherPatientIDsSequence))

# ds.PatientName = None
# print(elem)
# ds.OtherPatientIDsSequence = None
# print(len(ds.OtherPatientIDsSequence))

# Adding elements
# Any category
# print(dictionary_VR([0x0028, 0x1050]))
# ds.add_new([0x0028, 0x1050], 'DS', '100.0')
# elem = ds[0x0028, 0x1050]
# print(elem)

# Standard elements
print('WindowWidth' in ds)
ds.WindowWidth = 500
print(ds['WindowWidth'])
print([0x0043, 0x104E] in ds)


# Sequences
seq = ds.OtherPatientIDsSequence
seq += [Dataset(), Dataset(), Dataset()]
seq[0].PatientID = 'Citizen^Jan'
seq[0].TypeOfPatientID = 'TEXT'
seq[1].PatientID = 'CompressedSamples^CT1'
seq[1].TypeOfPatientID = 'TEXT'
print(seq[0])
print(seq[1])


# Delete Elements
print([0x0043, 0x104E] in ds)
del ds[0x0043, 0x104E]
print([0x0043, 0x104E] in ds)

# del ds.WindowCenter
# print('WindowCenter' in ds)

# remove items from sequences and multi-valued elements using your preferred list method
del ds.OtherPatientIDsSequence[2]
print(len(seq))
del ds.ImageType[2]
print(ds.ImageType)

ds.save_as('out.dcm')

# Other ways to save changes
# with open('out.dcm', 'wb') as outfile:
#    ds.save_as(outfile)

# from io import BytesIO
# out = BytesIO()
# ds.save_as(out)
