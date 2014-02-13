poly-open
=========

Simple python package that monkeypatches __builtin__.open so that it recognizes hdfs:, s3:, and other special file systems that would otherwise require anything that uses "open" to know about them.
