use SALEDATA001 
DECLARE @a VARCHAR(10);
DECLARE @b VARCHAR(10)
SET
  @a = '2018-01-01' --选择年份
SET
  @b = '2018-05-31' --选择月份
select
  *
from
  (
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆入库' AS 单据类型
    FROM
      CARIN
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARIN.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆销售' AS 单据类型
    FROM
      CARXS
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARXS.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(loginno) AS 单据数量,
      dptname AS 部门,
      '维修' AS 单据类型
    FROM
      LOGINREPAIR
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = LOGINREPAIR.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '三包索赔出库' AS 单据类型
    FROM
      SBSPH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = SBSPH.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件采购入库' AS 单据类型
    FROM
      WAREINH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = WAREINH.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件销售出库' AS 单据类型
    FROM
      WAREOUTH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = WAREOUTH.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '收款文件' AS 单据类型
    FROM
      INCOMECURR
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = INCOMECURR.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '收款折让文件' AS 单据类型
    FROM
      INCOMEDISC
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = INCOMEDISC.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '其他费用' AS 单据类型
    FROM
      OTHERCHARGE
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = OTHERCHARGE.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '其他收付款' AS 单据类型
    FROM
      OTHERINCOME
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = OTHERINCOME.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '付款折让文件' AS 单据类型
    FROM
      PAYDISC
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = PAYDISC.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '付款文件' AS 单据类型
    FROM
      PAYCURR
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = PAYCURR.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件采购退货' AS 单据类型
    FROM
      REFUNDINH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = REFUNDINH.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件销售退货' AS 单据类型
    FROM
      REFUNDOUTH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = REFUNDOUTH.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '维修收款' AS 单据类型
    FROM
      REPAIRCURR
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = REPAIRCURR.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件调拨' AS 单据类型
    FROM
      WAREALLOTH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = WAREALLOTH.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件调拨' AS 单据类型
    FROM
      WAREALLOTH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = WAREALLOTH.dptno
    WHERE
      date0 BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆调价' AS 单据类型
    FROM
      CARADJUST
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARADJUST.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆调拨' AS 单据类型
    FROM
      CARALLOT
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARALLOT.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆合同' AS 单据类型
    FROM
      CARHTXS
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARHTXS.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆采购退货' AS 单据类型
    FROM
      CARRETIN
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARRETIN.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '车辆销售退货' AS 单据类型
    FROM
      CARRETXS
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = CARRETXS.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件其他入库' AS 单据类型
    FROM
      OTHERINH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = OTHERINH.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
    UNION ALL
    SELECT
      count(noteno) AS 单据数量,
      dptname AS 部门,
      '配件其他出库' AS 单据类型
    FROM
      OTHEROUTH
      INNER JOIN DEPARTMENT ON DEPARTMENT.dptno = OTHEROUTH.dptno
    WHERE
      notedate BETWEEN @a
      AND @b
    GROUP BY
      dptname
  ) as t
where
  t.部门like '万州%'