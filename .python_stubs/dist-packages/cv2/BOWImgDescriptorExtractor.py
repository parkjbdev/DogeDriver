# encoding: utf-8
# module cv2
# from /usr/lib/python3/dist-packages/cv2.cpython-38-x86_64-linux-gnu.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2 as  # <module 'cv2'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.aruco as aruco # <module 'cv2.aruco'>
import cv2.bgsegm as bgsegm # <module 'cv2.bgsegm'>
import cv2.bioinspired as bioinspired # <module 'cv2.bioinspired'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.datasets as datasets # <module 'cv2.datasets'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.dynafu as dynafu # <module 'cv2.dynafu'>
import cv2.face as face # <module 'cv2.face'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.freetype as freetype # <module 'cv2.freetype'>
import cv2.ft as ft # <module 'cv2.ft'>
import cv2.hdf as hdf # <module 'cv2.hdf'>
import cv2.hfs as hfs # <module 'cv2.hfs'>
import cv2.img_hash as img_hash # <module 'cv2.img_hash'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.kinfu as kinfu # <module 'cv2.kinfu'>
import cv2.line_descriptor as line_descriptor # <module 'cv2.line_descriptor'>
import cv2.linemod as linemod # <module 'cv2.linemod'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.motempl as motempl # <module 'cv2.motempl'>
import cv2.multicalib as multicalib # <module 'cv2.multicalib'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.omnidir as omnidir # <module 'cv2.omnidir'>
import cv2.optflow as optflow # <module 'cv2.optflow'>
import cv2.plot as plot # <module 'cv2.plot'>
import cv2.ppf_match_3d as ppf_match_3d # <module 'cv2.ppf_match_3d'>
import cv2.quality as quality # <module 'cv2.quality'>
import cv2.reg as reg # <module 'cv2.reg'>
import cv2.rgbd as rgbd # <module 'cv2.rgbd'>
import cv2.saliency as saliency # <module 'cv2.saliency'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.structured_light as structured_light # <module 'cv2.structured_light'>
import cv2.text as text # <module 'cv2.text'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.videostab as videostab # <module 'cv2.videostab'>
import cv2.viz as viz # <module 'cv2.viz'>
import cv2.ximgproc as ximgproc # <module 'cv2.ximgproc'>
import cv2.xphoto as xphoto # <module 'cv2.xphoto'>

from .object import object

class BOWImgDescriptorExtractor(object):
    # no doc
    def compute(self, image, keypoints, imgDescriptor=None): # real signature unknown; restored from __doc__
        """
        compute(image, keypoints[, imgDescriptor]) -> imgDescriptor
        .   @overload
        .       @param keypointDescriptors Computed descriptors to match with vocabulary.
        .       @param imgDescriptor Computed output image descriptor.
        .       @param pointIdxsOfClusters Indices of keypoints that belong to the cluster. This means that
        .       pointIdxsOfClusters[i] are keypoint indices that belong to the i -th cluster (word of vocabulary)
        .       returned if it is non-zero.
        """
        pass

    def descriptorSize(self): # real signature unknown; restored from __doc__
        """
        descriptorSize() -> retval
        .   @brief Returns an image descriptor size if the vocabulary is set. Otherwise, it returns 0.
        """
        pass

    def descriptorType(self): # real signature unknown; restored from __doc__
        """
        descriptorType() -> retval
        .   @brief Returns an image descriptor type.
        """
        pass

    def getVocabulary(self): # real signature unknown; restored from __doc__
        """
        getVocabulary() -> retval
        .   @brief Returns the set vocabulary.
        """
        pass

    def setVocabulary(self, vocabulary): # real signature unknown; restored from __doc__
        """
        setVocabulary(vocabulary) -> None
        .   @brief Sets a visual vocabulary.
        .   
        .       @param vocabulary Vocabulary (can be trained using the inheritor of BOWTrainer ). Each row of the
        .       vocabulary is a visual word (cluster center).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


