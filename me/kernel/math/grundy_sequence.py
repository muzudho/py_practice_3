from kernel.math.mex import mex


class GrundySequence:
    """グランディ数列

    X軸上の任意の１点だけのグランディ数が欲しい、ということはできず、
    グランディ数は、原点から X軸上の任意の点までのグランディ数の配列として用意される"""

    @staticmethod
    def make(S: set, len_N: int):
        """グランディ数生成アルゴリズム

        Parameters
        ----------
        len_N : int
            山の石の数（ゲーム上、最大数）
        S : set
            サブトラクションセット

        Returns
        -------
        grundy_sequence : GrundySequence
        """

        # グランディ数の配列のサイズ確定。 0 を含めるので 1 足す
        len_Nz = len_N + 1
        sequence = [0] * len_Nz

        # 昇順ソート a < b < c
        S_list = list(S)
        S_list.sort()

        for i in range(0, len_Nz):
            """i は局面の石の数"""

            T = []
            """T は 隣接する遷移先のグランディ数のリスト"""

            for s in S_list:
                """s は 除去可能数"""

                ti = i-s
                """ti は 遷移先の局面の石の数"""

                if ti < 0:
                    # 石の数が負数の局面は無いのでスキップ
                    continue

                t = sequence[ti]
                """t は 遷移先の局面のグランディ数"""

                T.append(t)

            grundy = mex(T)
            """grundy は、この局面のグランディ数"""

            sequence[i] = grundy

        return GrundySequence(sequence, S_list)

    def __init__(self, sequence: list, S_list: list):

        self.__sequence = sequence
        """添え字は、盤上の石の数 n （ 0 ～ len(N) ）"""

        self.__S_list = S_list
        """サブストラクションセット"""

    @property
    def len(self):
        return len(self.__sequence)

    @property
    def S_list(self):
        return self.__S_list

    def get_grundy_at(self, i: int):
        """グランディ数

        Parameters
        ----------
        i : int
            局面の石の数
        """
        return self.__sequence[i]

    def get_bit_grundy_at(self, i: int):
        """ビット グランディ数

        Parameters
        ----------
        i : int
            局面の石の数
        """
        if self.__sequence[i] == 0:
            return 0

        return 1
